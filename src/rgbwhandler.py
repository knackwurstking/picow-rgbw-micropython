from picozero import pico_temp_sensor

import info
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


def device():
    """Method used for a device scan"""
    header = "HTTP/1.0 200 OK\r\nContent-Type: text/text\r\n\r\n"
    body = f"{info.APPLICATION}_v{info.VERSION}\n"
    return header, body


def info_page():
    header = "HTTP/1.0 200 OK\r\nContent-Type: text/text\r\n\r\n"

    body = f"""\
Device: {info.APPLICATION}_v{info.VERSION}

Temp: {pico_temp_sensor.temp}

Freq: {rgbw.freq}
Duty Range: 0-100 (%)

| Color   | Pin | Duty |
|---------|-----|------|
"""

    if "r" in rgbw.pins:
        pin = rgbw.pins["r"]
        body += f"| [r]ed   | {pin.pin: 3} | {pin.get_duty_cycle(): 4} |\n"
    else:
        body += "| [r]ed   | --- | ---- |\n"

    if "g" in rgbw.pins:
        pin = rgbw.pins["g"]
        body += f"| [g]reen | {pin.pin: 3} | {pin.get_duty_cycle(): 4} |\n"
    else:
        body += "| [g]reen | --- | ---- |\n"

    if "b" in rgbw.pins:
        pin = rgbw.pins["b"]
        body += f"| [b]lue  | {pin.pin: 3} | {pin.get_duty_cycle(): 4} |\n"
    else:
        body += "| [b]lue  | --- | ---- |\n"

    if "w" in rgbw.pins:
        pin = rgbw.pins["w"]
        body += f"| [w]hite | {pin.pin: 3} | {pin.get_duty_cycle(): 4} |\n"
    else:
        body += "| [w]hite | --- | ---- |\n"

    return header, body
