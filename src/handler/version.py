import config


def version() -> str:
    return f"{config.DEVICE} {config.LANGUAGE} v{config.VERSION}"
