import log
import rgbw


def rgbw_color_get(_args: list[str]) -> str:
    pins_color: list[str] = ["-1", "-1", "-1", "-1"]

    for idx, color in enumerate(["r", "g", "b", "w"]):
        if color in rgbw.pins:
            pins_color[idx] = str(rgbw.pins[color].get_duty_cycle())

    return " ".join(pins_color) + "\n"


def rgbw_color_set(args: list[str]) -> None:
    pins_color: list[int] = [0, 0, 0, 0]

    # parse args
    for idx, color in enumerate(args):
        try:
            pins_color[idx] = int(color)
        except Exception as err:
            log.error(f"exception: {str(err)}")
            return None

    # add color duty cycle to rgbw
    for idx, color in enumerate(["r", "g", "b", "w"]):
        pin = rgbw.get(color)

        if pin is not None:
            pin.set_duty_cycle(pins_color[idx])

    return None


def rgbw_gp_get(_args: list[str]) -> str:
    pins_rgbw: list[str] = ["-1", "-1", "-1", "-1"]

    for idx, color in enumerate(["r", "g", "b", "w"]):
        if color in rgbw.pins:
            pins_rgbw[idx] = str(rgbw.pins[color].pin)

    return " ".join(pins_rgbw) + "\n"


def rgbw_gp_set(args: list[str]) -> None:
    """..."""
    pins_rgbw = [0, 0, 0, 0]

    # parse args
    for idx, pin in enumerate(args):
        try:
            pins_rgbw[idx] = int(pin)
        except Exception as err:
            log.error(f"exception: {str(err)}")
            return None

    # add pin to rgbw
    for idx, color in enumerate(["r", "g", "b", "w"]):
        rgbw.remove(color)
        rgbw.add(color, pins_rgbw[idx])

    return None
