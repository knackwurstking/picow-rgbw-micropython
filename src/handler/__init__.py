from typing import Callable

from handler.device import device_pwm_freq
from handler.device import device_pwm_range
from handler.device import device_server_get
from handler.device import device_server_set
from handler.info import info_temp
from handler.rgbw import rgbw_color_get
from handler.rgbw import rgbw_color_set
from handler.rgbw import rgbw_gp_get
from handler.rgbw import rgbw_gp_set
from handler.version import version

commands: dict[
    str,
    dict[
        str,
        dict[
            str,
            dict[
                str,
                Callable[[], None | str]
            ] | Callable[[], None | str]
        ] | Callable[[], None | str]
    ] | Callable[[], None | str]
] = {
    "rgbw": {
        "color": {
            "get": rgbw_color_get,
            "set": rgbw_color_set,
        },
        "gp": {
            "get": rgbw_gp_get,
            "set": rgbw_gp_set,
        },
    },
    "version": version,
    "info": {
        "temp": info_temp,
    },
    "device": {
        "pwm": {
            "range": device_pwm_range,
            "freq": device_pwm_freq,
        },
        "server": {
            "get": device_server_get,
            "set": device_server_set,
        },
    },
}


def request_handler(req: str) -> None | str:
    """TCP request handler...

    Each command is separated with a '\\n' or a ';'

    Get/Set RGBW color, in range from 0 to 100.
    >>> rgbw color set 100 100 100 100
    >>> rgbw color get
    100 100 100 100

    Get/Set gp (GPIO pins) in use for rgbw
    >>> rgbw gp set 0 1 2 3
    >>> rgbw gp get
    0 1 2 3

    Get device identification string (`<device> <language> <version>`)
    >>> version
    picow micropython v0.0.1

    Get device temperature
    >>> info temp
    22.8311

    Get disk usage info (`<used> <free>`)
    >>> info disk-usage

    Get device logs
    >>> log get
    [DEBUG] ...
    [ INFO] ...
    ...

    Enable/Disable debugging
    >>> log debug enable
    >>> log debug disable

    Clear all device logs
    >>> log clear

    Get device pwm range (`<min %> <max %>`)
    >>> device pwm range
    0 100

    Get device pwm frequency
    >>> device pwm freq
    1000

    Get/Set the web server for registration on after boot
    >>> device server set http://192.168.178.20:50833
    >>> device server get
    http://192.168.178.20:50833

    """
    # split request on "\n" and ";" to get commands
    req_split: list[str] = []
    for part in req.split("\n"):
        for command in part.split(";"):
            req_split.append(command)

    # TODO: split command on space(s) " "

    # TODO: search for command and run or just close on error
