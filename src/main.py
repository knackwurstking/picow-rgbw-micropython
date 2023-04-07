import contextlib
import gc
import socket
from time import sleep

#import micropython
import machine
import network
from picozero import pico_led

import config
import handler


def connect():
    """Connect to WLAN (ssid, password)"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm=0xa11140)  # disable power-save mode
    wlan.connect(config.SSID, config.PASSWORD)

    # Wait for connection
    while wlan.isconnected() is False:
        sleep(1)

    return wlan.ifconfig()[0]


def open_socket(ip):
    """Open a socket."""
    a = (ip, config.PORT)
    c = socket.socket()
    c.bind(a)
    c.listen(1)
    return c


def serve(c):
    """Start the web server"""
    pico_led.on()
    gc.collect()
    gc.disable()

    while True:
        #micropython.mem_info()
        client = c.accept()[0]

        try:
            header, body = handle_request(str(client.recv(1024)))
            if header:
                client.send(header)
            if body:
                client.send(body)
        finally:
            client.close()
            gc.collect()


def handle_request(req: str):
    method: str = ""
    pathname: str = ""
    query: list[str] = []

    with contextlib.suppress(IndexError):
        method, pathname, query = handler.utils.parse_request(req)

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
    ip = connect()

    c = open_socket(ip)

    # Register this device on the server
    config.load()
    config.register_to_server(ip)

    try:
        serve(c)
    finally:
        pico_led.off()
        c.close()
finally:
    machine.reset()
