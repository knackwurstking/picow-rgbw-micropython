import contextlib

import handler
import log
import machine
import server
import utime
import wifi
from picozero import pico_led


def request_handler(req: str):
    # TODO: read data from request (json unmarshal)
    # data format: `{ command: str, options: dict }`

    # TODO: run command with options

    # TODO: return json data or close on empty response

    pass


def request_handler_web(req: str):
    method: str = ""
    pathname: str = ""
    query: list[str] = []

    with contextlib.suppress(IndexError):
        method, pathname, query = handler.utils.parse_request(req)

    log.debug(f"method={method} | pathname={pathname} | query={query}\n")

    if pathname[:13] == "/rgbw/set_pin" and method == "POST":
        return handler.rgbw.post_pin(handler.utils.parse_query(query))

    if pathname[:13] == "/rgbw/set_pwm" and method == "POST":
        return handler.rgbw.post_pwm(handler.utils.parse_query(query))

    if pathname[:14] == "/rgbw/get_pins" and method == "GET":
        return handler.rgbw.get_pins()

    if pathname[:14] == "/rgbw/get_duty" and method == "GET":
        return handler.rgbw.get_duty()

    if pathname[:14] == "/server" and method == "GET":
        return handler.server.get()

    if pathname[:14] == "/server" and method == "POST":
        return handler.server.post(handler.utils.parse_query(query))

    if pathname[:7] == "/device" and method == "GET":
        return handler.root.get_device()

    if pathname[:1] == "/" and method == "GET":
        return handler.root.get_info_page()

    return handler.utils.response("404 NOT FOUND")


try:
    wifi.start()

    pico_led.on()

    sock = server.open()
    server.serve(sock, request_handler)
except Exception as e:
    print(e)
    log.error(str(e) + "\n")
finally:
    machine.reset()
    utime.sleep(1)
