import config

from handler import utils


def get():
    return utils.response(
        "200 OK",
        f'{config.SERVER["protocol"]}//{config.SERVER["host"]}:{config.SERVER["port"]}\n'
    )


def post(query: dict[str, str]):
    print(query, config.SERVER)
    status = "200 OK"

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

    if status == "200 OK":
        if query["protocol"]:
            config.SERVER["protocol"] = query["protocol"]

        if query["host"]:
            config.SERVER["host"] = query["host"]

        if query["port"]:
            config.SERVER["port"] = int(query["port"])

        config.save()

    return utils.response(status)
