import config


def version(args: list[str]) -> str:
    """..."""
    return f"{config.DEVICE} {config.LANGUAGE} v{config.VERSION}"
