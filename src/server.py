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
        gc.collect()

        log.debug("waiting for client...")
        client = sock.accept()[0]

        try:
            resp = handler(str(client.recv(1024)))
            log.debug(f"got response: {resp}")
            if resp is not None:
                client.send(resp)
        except Exception as err:
            log.error(f"exception: {err}")
        finally:
            client.close()
