from picozero import pico_temp_sensor

import info
import rgbw


def set_rgbw_pin(query: dict[str, str]):
    http_status = "200 OK"

    for color in query:
        if color in ["r", "g", "b", "w"]:
            try:
                rgbw.add(color, int(query[color]))
                c = rgbw.get(color)
                if c is not None:
                    print(c[1])
            finally:
                http_status = "500 INTERNAL SERVER ERROR"
                continue

    header = f"HTTP/1.0 {http_status}\r\nContent-Type: text/text\r\n\r\n"
    return header, ""


def set_rgbw_pwm(query: dict[str, str]):
    http_status = "200 OK"

    for color, value in query.items():
        if color in ["r", "g", "b", "w"]:
            try:
                rgbw.set(color, int(value))
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

R: {rgbw.rgbw["r"][0] if "r" in rgbw.rgbw else "None"} {
        rgbw.rgbw["r"][1].duty() if "r" in rgbw.rgbw else "-"}
G: {rgbw.rgbw["g"][0] if "g" in rgbw.rgbw else "None"} {
        rgbw.rgbw["g"][1].duty() if "g" in rgbw.rgbw else "-"}
B: {rgbw.rgbw["b"][0] if "b" in rgbw.rgbw else "None"} {
        rgbw.rgbw["b"][1].duty() if "b" in rgbw.rgbw else "-"}
W: {rgbw.rgbw["w"][0] if "w" in rgbw.rgbw else "None"} {
        rgbw.rgbw["w"][1].duty() if "w" in rgbw.rgbw else "-"}
"""
    return header, body
