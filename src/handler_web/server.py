import config

from handler import utils


def get():
    return utils.response(
        "200 OK",
        f'{config.SERVER["protocol"]}//{config.SERVER["host"]}:{config.SERVER["port"]}\n'
    )


def post(query: dict[str, str]):
    status = "200 OK"

    if query.get("protocol") in ["http:", "https:"]:
        config.SERVER["protocol"] = query.get("protocol")

    if query.get("host"):
        config.SERVER["host"] = query.get("host")

    if query.get("port"):
        try:
            config.SERVER["port"] = int(query["port"])
        except Exception:
            status = "400 BAD REQUEST"

    if status == "200 OK":
        config.save()

    return utils.response(status)
