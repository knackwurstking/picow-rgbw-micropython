import os.path

import config


def get() -> str:
    """Get pico log"""
    if not os.path.exists("pico.log"):
        return ""

    with open("pico.log", "r", encoding="utf-8") as file:
        return file.read()


def log(message: str) -> None:
    """..."""
    with open("pico.log", "a", encoding="utf-8") as file:
        file.write(message + "\n")


def debug(message: str) -> None:
    """..."""
    if not config.DEBUG:
        return

    log("DEBUG:" + message)


def error(message: str) -> None:
    """..."""
    log("ERROR:" + message)
