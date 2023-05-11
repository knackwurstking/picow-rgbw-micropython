import log
import rgbw


def rgbw_color_get(args: list[str]) -> None:
    """..."""


def rgbw_color_set(args: list[str]) -> None:
    """..."""


def rgbw_gp_get(args: list[str]) -> None:
    """..."""


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
