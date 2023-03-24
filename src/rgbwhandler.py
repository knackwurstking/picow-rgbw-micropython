import rgbw


def set_pin(query: dict[str, str]):
    http_status = "200 OK"

    for color in query:
        if color in ["r", "g", "b", "w"]:
            try:
                rgbw.add(color, int(query[color]))
            finally:
                http_status = "500 INTERNAL SERVER ERROR"
                continue

    header = f"HTTP/1.0 {http_status}\r\nContent-Type: text/text\r\n\r\n"
    return header, ""


def set_pwm(query: dict[str, str]):
    http_status = "200 OK"

    for color, value in query.items():
        if color in ["r", "g", "b", "w"]:
            try:
                if pin := rgbw.get(color):
                    pin.set_duty_cycle(int(value))
            finally:
                http_status = "500 INTERNAL SERVER ERROR"

    header = f"HTTP/1.0 {http_status}\r\nContent-Type: text/text\r\n\r\n"
    return header, ""
