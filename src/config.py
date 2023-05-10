import contextlib

import requests

DEBUG: bool = False

SSID: str = ""
PASSWORD: str = ""

DEVICE: str = "picow"
LANGUAGE: str = "micropython"
VERSION: str = "0.0.1"

PORT: int = 80

SERVER_UPDATE_PATH: str = "/api/v1/picow"
SERVER: str = ""

PWM_FREQ = 1000


def register_to_server(ip: str) -> None:
    """..."""
    if SERVER == "":
        return

    requests.post(f'{SERVER}{SERVER_UPDATE_PATH}',
                  json={"addr": f"{ip}:{PORT}"})


def save() -> None:
    """..."""
    if SERVER == "":
        return

    with open("server.json", "w", encoding="utf-8") as file:
        file.write(SERVER)


def load() -> None:
    """..."""
    global SERVER

    with contextlib.suppress(Exception):
        with open("server.json", "r", encoding="utf-8") as file:
            SERVER = file.read().strip(" \n")
