import rgbw


def set_pin(query: dict[str, str]):
    http_status = "200 OK"

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
            except Exception as e:
                http_status = "500 INTERNAL SERVER ERROR"
                print(e)

    if http_status == "200 OK":
        try:
            rgbw.save()
        finally:
            pass

    header = f"HTTP/1.0 {http_status}\r\nContent-Type: text/text\r\n\r\n"
    return header, ""


def set_pwm(query: dict[str, str]):
    http_status = "200 OK"

    for color, value in query.items():
        if color in ["r", "g", "b", "w"]:
            try:
                if pin := rgbw.get(color):
                    pin.set_duty_cycle(int(value))
            except Exception as e:
                http_status = "500 INTERNAL SERVER ERROR"
                print(e)

    header = f"HTTP/1.0 {http_status}\r\nContent-Type: text/text\r\n\r\n"
    return header, ""


def get_pins():
    header = "HTTP/1.0 200 OK\r\nContent-Type: text/text\r\n\r\n"
    body = ""

    for color in ["r", "g", "b", "w"]:
        if color in rgbw.pins:
            pin = rgbw.pins[color]
            body += f"{pin.pin} "
        else:
            body += "-1 "

    body = body.rstrip(" ") + "\n"

    return header, body


def get_duty():
    header = "HTTP/1.0 200 OK\r\nContent-Type: text/text\r\n\r\n"
    body = ""

    for color in ["r", "g", "b", "w"]:
        if color in rgbw.pins:
            pin = rgbw.pins[color]
            body += f"{pin.get_duty_cycle()} "
        else:
            body += "-1 "

    body = body.rstrip(" ") + "\n"

    return header, body
