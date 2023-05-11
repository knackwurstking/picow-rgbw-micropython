import config


def device_pwm_range(_args: list[str]) -> str:
    """..."""
    return "0 100"


def device_pwm_freq(_args: list[str]) -> str:
    """..."""
    return f"{config.PWM_FREQ}"


def device_server_get(_args: list[str]) -> str:
    """..."""
    return config.SERVER


def device_server_set(args: list[str]) -> None:
    """..."""
    if len(args) == 1:
        config.SERVER = args[0]
