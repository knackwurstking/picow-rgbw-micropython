import config


def log(message: str) -> None:
    """..."""
    with open("pico.log", "a", encoding="utf-8") as file:
        file.write(message)


def debug(message: str) -> None:
    """..."""
    if not config.DEBUG:
        return

    log("DEBUG:" + message)


def error(message: str) -> None:
    """..."""
    log("ERROR:" + message)
