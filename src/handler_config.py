import config

def get_server():
    header = "HTTP/1.0 200 OK\r\nContent-Type: text/text\r\n\r\n"
    body = f'{config.SERVER["protocol"]}//{config.SERVER["host"]}:{config.SERVER["port"]}'

    return header, body

def post_server():
    http_status = "200 OK"

    # TODO: read body data (content-type: "text/text")
    # TODO: validate data (protocol, host and port)
    # TODO: store and register on server `config.register_to_server()`

    header = f"HTTP/1.0 {http_status}\r\nContent-Type: text/text\r\n\r\n"
    body = ""

    return header, body
