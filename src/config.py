import contextlib
import json

import urequests

DEBUG = False

SSID = ""
PASSWORD = ""

APPLICATION = "picow_micropython"
VERSION = "0.0.1"

PORT = 80

UPDATE_PATH = "/api/v1/picow"

SERVER = {
    "protocol": "http:",
    "host": "",
    "port": 50833,
}


def register_to_server(ip: str):
    if SERVER.get("protocol") and SERVER.get("host") and SERVER.get("port"):
        with contextlib.suppress(Exception):
            urequests.post(
                f'{SERVER["protocol"]}//{SERVER["host"]}:{SERVER["port"]}{UPDATE_PATH}',
                json={
                    "addr": f"{ip}:{PORT}"
                }
            )


def save():
    if SERVER.get("protocol") and SERVER.get("host") and SERVER.get("port"):
        with open("server.json", "w") as c:
            c.write(json.dumps(SERVER))


def load():
    global SERVER

    with contextlib.suppress(Exception):
        with open("server.json", "r") as c:
            SERVER = json.load(c)
