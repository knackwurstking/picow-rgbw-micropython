from .. import rgbw
from . import utils


def post_pin(query: dict[str, str]):
    status = "200 OK"

    for color, value in query.items():
        if color in ["r", "g", "b", "w"]:
            try:
                value = int(value)

                if color in rgbw.pins:
                    if value < 0:
                        rgbw.remove(color)
                        continue
                    elif value == rgbw.pins[color].pin:
                        # skip
                        continue

                rgbw.add(color, value)
            except Exception:
                status = "500 INTERNAL SERVER ERROR"

    if status == "200 OK":
        try:
            rgbw.save()
        finally:
            pass

    return utils.response(status)


def post_pwm(query: dict[str, str]):
    status = "200 OK"

    for color, value in query.items():
        if color in ["r", "g", "b", "w"]:
            try:
                if pin := rgbw.get(color):
                    pin.set_duty_cycle(int(value))
            except Exception:
                status = "500 INTERNAL SERVER ERROR"

    return utils.response(status)


def get_pins():
    body = ""

    for color in ["r", "g", "b", "w"]:
        if color in rgbw.pins:
            pin = rgbw.pins[color]
            body += f"{pin.pin} "
        else:
            body += "-1 "

    body = body.rstrip(" ") + "\n"

    return utils.response("200 OK", body)


def get_duty():
    body = ""

    for color in ["r", "g", "b", "w"]:
        if color in rgbw.pins:
            pin = rgbw.pins[color]
            body += f"{pin.get_duty_cycle()} "
        else:
            body += "-1 "

    body = body.rstrip(" ") + "\n"

    return utils.response("200 OK", body)
