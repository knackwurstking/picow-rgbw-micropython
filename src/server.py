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

        resp = handler(client.recv(1024))
        if resp:
            client.send(resp)

        client.close()
