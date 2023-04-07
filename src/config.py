import contextlib

import urequests

SSID = ""
PASSWORD = ""

APPLICATION = "picow_micropython"
VERSION = "0.0.1"

PORT = 80

SERVER_URL = "http://192.168.178.20:50833"

UPDATE_PATH = "/api/v1/picow"

# TODO: SERVER will replace the SERVER_URL
SERVER = {
    "protocol": "http:",
    "host": "192.168.178.20",
    "port": 50833,
}


def register_to_server(ip: str):
    if SERVER_URL:
        with contextlib.suppress(Exception):
            urequests.post(
                SERVER_URL + UPDATE_PATH,
                json={
                    "addr": f"{ip}:{PORT}"
                }
            )
