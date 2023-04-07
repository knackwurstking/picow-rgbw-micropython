import contextlib
import socket
from time import sleep

import gc
#import micropython
import machine
import network
import urequests
from picozero import pico_led

import handler
import config
import rgbwhandler


def connect():
    """Connect to WLAN (ssid, password)"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm = 0xa11140)  # disable power-save mode
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
        # split http request (string)
        req_split = req.split()
        # get the method (fist element in request split)
        method = req_split[0].lstrip("b'")

        # get query from second element in request split (all after "?")
        query_split = req_split[1].split("?")
        if len(query_split) > 1:
            query = query_split[1].split("&")

        # get the server path to handle (first element in query split, before "?")
        pathname = query_split[0]

    # TODO: Adding route: GET "/config/server" => "application/json", { "protocol", "host", "port" }
    # TODO: Adding route: POST "/config/server", "application/json", { "protocol", "host", "port" }

    if pathname[:13] == "/rgbw/set_pin" and method == "POST":
        return rgbwhandler.set_pin(parse_query(query))

    if pathname[:13] == "/rgbw/set_pwm" and method == "POST":
        return rgbwhandler.set_pwm(parse_query(query))

    if pathname[:14] == "/rgbw/get_pins" and method == "GET":
        return rgbwhandler.get_pins()

    if pathname[:14] == "/rgbw/get_duty" and method == "GET":
        return rgbwhandler.get_duty()

    if pathname[:7] == "/device" and method == "GET":
        return handler.device()

    if pathname[:1] == "/" and method == "GET":
        return handler.info_page()

    return "HTTP/1.0 404 NOT FOUND\r\nContent-Type: text/text\r\n\r\n", ""


def parse_query(queries: list[str]):
    ql: dict[str, str] = {}

    for q in queries:
        name, value = q.split("=", 1)
        ql[name] = value

    return ql


try:
    ip = connect()

    c = open_socket(ip)

    # Register this device on the server
    if config.SERVER_URL:
        with contextlib.suppress(Exception):
            urequests.post(
                config.SERVER_URL + config.UPDATE_PATH,
                json={
                    "addr": f"{ip}:{config.PORT}"
                }
            )

    try:
        serve(c)
    finally:
        c.close()
finally:
    machine.reset()
