import config


def get() -> str:
    """Get pico log"""
    with open("pico.log", "r", encoding="utf-8") as file:
        return file.read()


def clear():
    """Remove all stuff from the pico.log file"""
    with open("pico.log", "w", encoding="utf-8") as file:
        file.write("")


def log(message):
    """..."""
    with open("pico.log", "a", encoding="utf-8") as file:
        file.write(message + "\n")


def debug(message):
    """..."""
    if not config.DEBUG:
        return

    log("DEBUG:" + message)


def error(message):
    """..."""
    log("ERROR:" + message)
