import gc
import socket
from typing import Callable

import config
import log


def create() -> socket.socket:
    """Open a socket."""
    address = ("0.0.0.0", config.PORT)
    sock = socket.socket()
    sock.bind(address)
    sock.listen(1)

    return sock


def serve(sock, handler: Callable[[str], None | str]) -> None:
    """..."""
    while True:
        log.debug("Waiting for client!\n")
        gc.collect()
        client = sock.accept()[0]

        resp = handler(str(client.recv(1024)))
        if resp is not None:
            client.send(resp)

        client.close()
