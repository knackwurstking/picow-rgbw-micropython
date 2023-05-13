import contextlib

import log
import urequests as requests

DEBUG: bool = False

SSID: str = ""
PASSWORD: str = ""

DEVICE: str = "picow"
LANGUAGE: str = "micropython"
VERSION: str = "0.0.1"

PORT: int = 8888

SERVER_UPDATE_PATH: str = "/api/v1/picow"
SERVER: str = ""

PWM_FREQ = 1000
PWM_DUTY_MIN = 0
PWM_DUTY_MAX = 100


def register_to_server(ip):
    """..."""
    if SERVER == "":
        return

    requests.post(f'{SERVER}{SERVER_UPDATE_PATH}',
                  json={"addr": f"{ip}:{PORT}"})


def save():
    """..."""
    if SERVER == "":
        return

    with open("server.json", "w", encoding="utf-8") as file:
        file.write(SERVER)


def load():
    """..."""
    global SERVER

    log.debug("load 'server.json' data (if exists)")

    with contextlib.suppress(Exception):
        with open("server.json", "r", encoding="utf-8") as file:
            SERVER = file.read().strip(" \n")
