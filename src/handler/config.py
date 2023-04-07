import config
from handler import utils


def get_server():
    return utils.response(
        "200 OK",
        f'{config.SERVER["protocol"]}//{config.SERVER["host"]}:{config.SERVER["port"]}\n'
    )


def post_server():
    status = "200 OK"
    body = ""

    # TODO: read body data (content-type: "text/text")
    # TODO: validate data (protocol, host and port)
    # TODO: store and register on server `config.register_to_server()`

    return utils.response(status, body)
