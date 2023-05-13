import gc
import socket

import config
import log


def create() -> socket.socket:
    """Open a socket."""
    address = ("0.0.0.0", config.PORT)
    sock = socket.socket()
    sock.bind(address)
    sock.listen(1)

    return sock


def serve(sock: socket.socket, handler_function):
    """

    sock: socket.socket
    handler_function: (str) -> None | str
    """
    while True:
        gc.collect()

        log.debug("waiting for client...")
        client = sock.accept()[0]

        try:
            data: str = client.recv(1024).decode("utf-8").strip()
            resp = handler_function(data)

            if resp is not None:
                client.send(resp)
        except Exception as err:
            log.error(f"exception: {err}")
        finally:
            client.close()
