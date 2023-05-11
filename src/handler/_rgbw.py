import log
import rgbw


def rgbw_color_get(_args: list[str]) -> str:
    """..."""
    pins_color: list[str] = ["-1", "-1", "-1", "-1"]

    for idx, color in enumerate(["r", "g", "b", "w"]):
        if color in rgbw.pins:
            pins_color[idx] = str(rgbw.pins[color].get_duty_cycle())

    return " ".join(pins_color)


def rgbw_color_set(args: list[str]) -> None:
    """..."""


def rgbw_gp_get(_args: list[str]) -> str:
    """..."""
    pins_rgbw: list[str] = ["-1", "-1", "-1", "-1"]

    for idx, color in enumerate(["r", "g", "b", "w"]):
        if color in rgbw.pins:
            pins_rgbw[idx] = str(rgbw.pins[color].pin)

    return " ".join(pins_rgbw)


def rgbw_gp_set(args: list[str]) -> None:
    """..."""
    pins_rgbw = [0, 0, 0, 0]

    for idx, pin in enumerate(args):
        try:
            pins_rgbw[idx] = int(pin)
        except Exception as err:
            log.error(f"exception: {str(err)}")
            return None

    for idx, color in enumerate(["r", "g", "b", "w"]):
        rgbw.remove(color)
        rgbw.add(color, pins_rgbw[idx])

    return None
