import contextlib

import urequests

DEBUG: bool = False

SSID: str = ""
PASSWORD: str = ""

DEVICE: str = "picow"
LANGUAGE: str = "micropython"
VERSION: str = "0.0.1"

PORT: int = 80

SERVER_UPDATE_PATH: str = "/api/v1/picow"
SERVER: str = ""


def register_to_server(ip: str):
    if SERVER == "":
        return

    urequests.post(f'{SERVER}{SERVER_UPDATE_PATH}',
                   json={"addr": f"{ip}:{PORT}"})


def save():
    if SERVER == "":
        return

    with open("server.json", "w", encoding="utf-8") as file:
        file.write(SERVER)


def load():
    global SERVER

    with contextlib.suppress(Exception):
        with open("server.json", "r", encoding="utf-8") as file:
            SERVER = file.read().strip(" \n")
