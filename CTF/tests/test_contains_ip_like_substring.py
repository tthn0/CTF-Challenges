from unittest import TestCase

from src.app.classes import Network


class TestContainsIPLikeSubstring(TestCase):
    def test_valid_ip_like_patterns(self) -> None:
        self.assertTrue(Network.contains_ip_like_substring("Hello from 192.168.1.1"))
        self.assertTrue(Network.contains_ip_like_substring("8.8.8.8 is cool"))
        self.assertTrue(Network.contains_ip_like_substring("https://0.0.0.0"))
        self.assertTrue(Network.contains_ip_like_substring("ftp://31.63.127.255:8080"))
        self.assertTrue(Network.contains_ip_like_substring("1000.2000.3000.4000"))
        self.assertTrue(Network.contains_ip_like_substring(".10.20.30.40."))
        self.assertTrue(Network.contains_ip_like_substring("192.168.001.1:080"))
        self.assertTrue(Network.contains_ip_like_substring("1.1.1.1.1:1"))
        self.assertTrue(Network.contains_ip_like_substring("0127.0000.0000.0001:1337"))
        self.assertTrue(Network.contains_ip_like_substring("000.111.222.333"))
        self.assertTrue(Network.contains_ip_like_substring("12345.67890.12345.67890"))
        self.assertTrue(Network.contains_ip_like_substring("before192.168.1.1"))
        self.assertTrue(Network.contains_ip_like_substring("192.168.1.1after"))
        self.assertTrue(Network.contains_ip_like_substring("192.168.1.1!"))

    def test_invalid_patterns(self) -> None:
        self.assertFalse(Network.contains_ip_like_substring("19216801"))
        self.assertFalse(Network.contains_ip_like_substring("192.168.1"))
        self.assertFalse(Network.contains_ip_like_substring("192.168.1."))
        self.assertFalse(Network.contains_ip_like_substring(".192.168.1"))
        self.assertFalse(Network.contains_ip_like_substring("192.168..1"))
        self.assertFalse(Network.contains_ip_like_substring("192..168.1"))
        self.assertFalse(Network.contains_ip_like_substring("192..168..1"))
        self.assertFalse(Network.contains_ip_like_substring("abc.168.0.1"))
        self.assertFalse(Network.contains_ip_like_substring("192.def.0.1"))
        self.assertFalse(Network.contains_ip_like_substring("Text with no IP..."))

    def test_empty_and_null_strings(self) -> None:
        self.assertFalse(Network.contains_ip_like_substring(""))
        self.assertRaises(TypeError, Network.contains_ip_like_substring, None)
