import config

from handler import utils


def get_server():
    return utils.response(
        "200 OK",
        f'{config.SERVER["protocol"]}//{config.SERVER["host"]}:{config.SERVER["port"]}\n'
    )


def post_server(query: dict[str, str]):
    status = "200 OK"
    body = ""

    if query["protocol"] not in ["http:", "https:"]:
        status = "400 BAD REQUEST"

    if not query["host"]:
        status = "400 BAD REQUEST"

    if not query["port"]:
        status = "400 BAD REQUEST"
    else:
        try:
            int(query["port"])
        except Exception:
            status = "400 BAD REQUEST"

    if status != "200 OK":
        config.SERVER["protocol"] = query["protocol"]
        config.SERVER["host"] = query["host"]

        if query["port"]:
            config.SERVER["port"] = int(query["port"])

        config.save()

    return utils.response(status, body)
