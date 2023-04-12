import contextlib
import gc
import socket

import machine
import network
import utime
from picozero import pico_led

import config
import handler

pico_log = open("pico.log", "w")


def connect():
    """Connect to WLAN (ssid, password)"""
    pico_log.write("Connecting wlan...\n")

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    #wlan.config(pm=0xa11140)  # disable power-save mode

    wlan.connect(config.SSID, config.PASSWORD)

    # Wait for connection
    while not wlan.isconnected():
        if not wait_for_wlan_connection(wlan):
            pico_log.write("...connection to wlan failed, try re-connecting...\n")
            wlan = connect()

    pico_log.write("...connection established.\n")
    return wlan


def wait_for_wlan_connection(wlan: network.WLAN):
    c = 0
    while wlan.isconnected() is False:
        utime.sleep(1)

        c += 1
        if c > 4:
            return False

    return True


def open_socket(ip):
    """Open a socket."""
    a = (ip, config.PORT)
    c = socket.socket()
    c.bind(a)
    c.listen(1)
    return c


def serve(c):
    """Start the web server"""
    while True:
        pico_log.write("Waiting for client!\n")
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

    pico_log.write(f"method={method} | pathname={pathname} | query={query}\n")

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
    wlan = connect()
    pico_led.on()
    ip = wlan.ifconfig()[0]
    c = open_socket(ip)

    # Register this device on the server
    config.load()
    config.register_to_server(ip)

    serve(c)
except Exception as e:
    print(e)
    pico_log.write(str(e) + "\n")
    utime.sleep(1)
finally:
    machine.reset()
    pico_log.close()
