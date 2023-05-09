import gc
import socket

import config
import log


def open():
    """Open a socket."""
    address = ("0.0.0.0", config.PORT)
    sock = socket.socket()
    sock.bind(address)
    sock.listen(1)
    return sock


def serve(sock, handler):
    while True:
        log.debug("Waiting for client!\n")
        gc.collect()
        client = sock.accept()[0]

        header, body = handler(str(client.recv(1024)))
        if header:
            client.send(header)
        if body:
            client.send(body)

        client.close()
