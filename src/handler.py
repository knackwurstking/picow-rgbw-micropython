from picozero import pico_temp_sensor

import info
import rgbw


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
