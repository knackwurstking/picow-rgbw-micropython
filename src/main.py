import contextlib
import gc
import socket

import _thread
import machine
import network
import utime
from picozero import pico_led

import config
import handler


def log(message: str):
    with open("pico.log", "a") as f:
        f.write(message)


def connect(wlan: network.WLAN, skip: bool = False):
    """Connect to WLAN (ssid, password)"""
    log("Connecting wlan...\n")

    wlan.active(True)
    #wlan.config(pm=0xa11140)  # disable power-save mode
    wlan.connect(config.SSID, config.PASSWORD)

    if skip:
        return wlan

    while not wlan.isconnected():
        if not wait_for_wlan_connection(wlan):
            log("...connection to wlan failed, try re-connecting...\n")
            wlan = connect(network.WLAN(network.STA_IF))

    log("...connection established.\n")

    # Register this device on the server
    config.load()
    config.register_to_server(wlan.ifconfig()[0])

    return wlan


def t_wifi(wlan: network.WLAN):
    while True:
        if not wlan.isconnected():
            wlan = connect(network.WLAN(network.STA_IF))
        else:
            utime.sleep(5)


def wait_for_wlan_connection(wlan: network.WLAN):
    c = 0
    while wlan.isconnected() is False:
        utime.sleep(1)

        c += 1
        if c > 4:
            return False

    return True


def open_socket():
    """Open a socket."""
    a = ("0.0.0.0", config.PORT)
    c = socket.socket()
    c.bind(a)
    c.listen(1)
    return c


def serve(c):
    """Start the web server"""
    while True:
        log("Waiting for client!\n")
        gc.collect()
        client = c.accept()[0]

        header, body = handle_request(str(client.recv(1024)))
        if header:
            client.send(header)
        if body:
            client.send(body)

        client.close()


def handle_request(req: str):
    method: str = ""
    pathname: str = ""
    query: list[str] = []

    with contextlib.suppress(IndexError):
        method, pathname, query = handler.utils.parse_request(req)

    log(f"method={method} | pathname={pathname} | query={query}\n")

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
    wlan = connect(network.WLAN(network.STA_IF))
    _thread.start_new_thread(t_wifi, (wlan,))

    pico_led.on()
    c = open_socket()

    serve(c)
except Exception as e:
    print(e)
    log(str(e) + "\n")
finally:
    machine.reset()
    utime.sleep(1)
