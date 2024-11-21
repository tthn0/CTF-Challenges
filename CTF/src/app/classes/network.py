from collections.abc import Callable
from ipaddress import AddressValueError, IPv4Address
from re import Match, match, search
from socket import error, gaierror, gethostbyname
from urllib.parse import ParseResult, unquote, urlparse

from flask.wrappers import Response as FlaskResponse
from requests import RequestException
from requests import Response as RequestsResponse
from requests import get
from requests.exceptions import RequestException

from .config import Config
from .token import Token


class NetworkError(Exception):
    __init__: Callable[..., None] = Exception.__init__


class Network:
    @staticmethod
    def is_invalid_url(url: str, token: str) -> str | None:
        if not url:
            return "Please provide a URL in the request body."
        elif "localhost" in url:
            return "URL may not contain `localhost`."
        elif "[" in url or "]" in url:
            return "URL may not contain square brackets."
        elif Network.contains_ip_like_substring(url):
            return "URL may not contain any IP addresses."

        if Token.get_status(token) == Token.STATUS.PRIVILEGED:
            if not Network.is_whitelisted_url(url):
                return f"Only URLs matching `{Config.DOMAIN_REGEX}` are allowed now."
            elif not Network.url_resolves_to_private_ipv4(url):
                return "External URLs are no longer allowed."
        elif str(Config.PORT) in url:
            return f"URL may not contain {Config.PORT}."

        return None

    @staticmethod
    def contains_ip_like_substring(string: str) -> bool:
        pattern: str = r"(\d+\.\d+\.\d+\.\d+)"
        matched: Match[str] | None = search(pattern, string)
        return bool(matched)

    @staticmethod
    def is_whitelisted_url(url: str) -> bool:
        pattern: str = Config.DOMAIN_REGEX
        decoded_url: str = unquote(url)
        matched: Match[str] | None = match(pattern, decoded_url)
        return bool(matched)

    @staticmethod
    def url_to_hostname(url: str) -> str | None:
        parsed_url: ParseResult = urlparse(url)
        return parsed_url.hostname

    @staticmethod
    def hostname_to_ip(hostname: str) -> IPv4Address:
        try:
            host: str = gethostbyname(hostname)
            return IPv4Address(host)
        except AddressValueError:
            raise NetworkError(
                f"`{hostname}` could not be resolved to an IPv4 address."
            )
        except gaierror:
            raise NetworkError(
                f"Failed to resolve `{hostname}`. It may not exist or is unreachable."
            )
        except error:
            raise NetworkError(
                f"An unexpected network error occurred while resolving `{hostname}`."
            )

    @staticmethod
    def url_resolves_to_private_ipv4(url: str) -> bool:
        hostname: str | None = Network.url_to_hostname(url)
        if hostname:
            ip: IPv4Address = Network.hostname_to_ip(hostname)
            return ip.is_private
        return False

    @staticmethod
    def fetch(url: str, token: str) -> FlaskResponse:
        try:
            response: RequestsResponse = get(
                url=url,
                cookies={"token": token},
                headers={"X-Secret-Key": Config.SECRET_KEY},
                timeout=5,
            )
            response.raise_for_status()
            return FlaskResponse(
                response=response.text,
                status=response.status_code,
                headers=response.headers,
            )
        except RequestException:
            raise NetworkError(f"Failed to fetch `{url}`.")
