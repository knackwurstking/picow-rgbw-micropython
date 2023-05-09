import config


def log(message: str):
    with open("pico.log", "a", encoding="utf-8") as file:
        file.write(message)


def debug(message: str):
    if not config.DEBUG:
        return

    log("DEBUG:" + message)


def error(message: str):
    log("ERROR:" + message)
