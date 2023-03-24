import contextlib
import socket
from time import sleep

import machine
import network
from picozero import pico_led

import handler
import info


def connect():
    """Connect to WLAN (ssid, password)"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(info.SSID, info.PASSWORD)

    # Wait for connection
    while wlan.isconnected() is False:
        print("Waiting for wlan connection...")
        sleep(1)

    return wlan.ifconfig()[0]


def open_socket(ip):
    """Open a socket."""
    a = (ip, 80)
    c = socket.socket()
    c.bind(a)
    c.listen(1)
    return c


def serve(c):
    """Start the web server"""
    pico_led.on()
    while True:
        client = c.accept()[0]

        try:
            header, body = handle_request(str(client.recv(1024)))
            if header:
                client.send(header)
            if body:
                client.send(body)
        finally:
            client.close()


def handle_request(req: str):
    header: str = "HTTP/1.0 404 NOT FOUND\r\nContent-Type: text/text\r\n\r\n"
    body: str = ""

    method: str = ""
    pathname: str = ""
    query: list[str] = []

    with contextlib.suppress(IndexError):
        req_split = req.split()
        method = req_split[0].lstrip("b'")
        query_split = req_split[1].split("?")
        if len(query_split) > 1:
            query = query_split[1].split("&")
        pathname = query_split[0]

    print(method, "|", pathname, "|", query)

    # POST: "/set_pin" ? r=<1-28> & g=<1-28> & b=<1-28> & w=<1-28>
    if pathname.startswith("/set_pin") and (method.upper() == "POST"):
        header, body = handler.set_pin(parse_query(query))

    # POST: "/set_pwm" ? r=<0-100%> & g=<0-100%> & b=<0-100%> & w=<0-100%>
    elif pathname.startswith("/set_pwm") and (method.upper() == "POST"):
        header, body = handler.set_pwm(parse_query(query))

    # GET: "/device" - device name
    elif pathname.startswith("/device") and (method.upper() == "GET"):
        header, body = handler.device()

    elif pathname == "/" and method.upper() == "GET":
        header, body = handler.info_page()

    return header, body


def parse_query(queries: list[str]):
    ql: dict[str, str] = {}

    for q in queries:
        name, value = q.split("=", 1)
        ql[name] = value

    return ql


try:
    info.IP = connect()
    print(f"WIFI connected on {info.IP}")

    c = open_socket(info.IP)
    try:
        serve(c)
    finally:
        c.close()
finally:
    machine.reset()
