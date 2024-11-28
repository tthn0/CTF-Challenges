from __future__ import annotations

import logging
from logging import Formatter, Handler
from pathlib import Path

from flask import request


class Logger:
    def __init__(
        self,
        log_directory: Path,
        log_file_name: str,
        output_to_console: bool = True,
        log_format: str = "[%(asctime)s] %(message)s",
    ) -> None:
        self.log_directory: Path = log_directory
        self.log_file_name: str = log_file_name
        self.output_to_console: bool = output_to_console
        self.log_format: str = log_format
        self.logger: logging.Logger = logging.getLogger(name=self.log_file_name)
        self._create_logger()

    @staticmethod
    def log_request(logger: Logger) -> None:
        logger.log(f"{request.method} {request.path}")
        logger.log(f"\tIP: `{request.remote_addr}`")
        logger.log(f"\tRequest Body: `{request.get_data(as_text=True)}`")

    def log(self, message: str, level: int = logging.INFO) -> None:
        self.logger.log(level=level, msg=message)

    def _create_logger(self) -> None:
        self.log_directory.mkdir(parents=True, exist_ok=True)

        if self.logger.hasHandlers():
            return

        handlers: list[Handler] = [
            logging.FileHandler(filename=self.log_directory / self.log_file_name)
        ]
        if self.output_to_console:
            handlers.append(logging.StreamHandler())

        formatter: Formatter = Formatter(fmt=self.log_format)
        for handler in handlers:
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.logger.setLevel(logging.INFO)
