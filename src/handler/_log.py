import config
import log


def log_get(_args: list[str]) -> str:
    """..."""
    return log.get()


def log_clear(_args: list[str]) -> None:
    """..."""
    log.clear()


def log_debug_enable(_args: list[str]) -> None:
    """..."""
    config.DEBUG = True


def log_debug_disable(_args: list[str]) -> None:
    """..."""
    config.DEBUG = False
