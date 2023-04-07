import config

from handler import utils


def get():
    return utils.response(
        "200 OK",
        f'{config.SERVER["protocol"]}//{config.SERVER["host"]}:{config.SERVER["port"]}\n'
    )


def post(query: dict[str, str]):
    status = "200 OK"

    if query.get("protocol") not in ["http:", "https:"]:
        status = "400 BAD REQUEST"
    else:
        config.SERVER["protocol"] = query.get("protocol")

    if not query.get("host"):
        status = "400 BAD REQUEST"
    else:
        config.SERVER["host"] = query.get("host")

    if not query.get("port"):
        status = "400 BAD REQUEST"
    else:
        try:
            config.SERVER["port"] = int(query["port"])
        except Exception:
            status = "400 BAD REQUEST"

    if status == "200 OK":
        config.save()

    return utils.response(status)
