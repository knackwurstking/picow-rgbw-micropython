import log
from handler._device import device_pwm_freq
from handler._device import device_pwm_range
from handler._device import device_server_get
from handler._device import device_server_set
from handler._info import info_disk_usage
from handler._info import info_temp
from handler._log import log_clear
from handler._log import log_debug_disable
from handler._log import log_debug_enable
from handler._log import log_get
from handler._rgbw import rgbw_color_get
from handler._rgbw import rgbw_color_set
from handler._rgbw import rgbw_gp_get
from handler._rgbw import rgbw_gp_set
from handler._version import version

commands = {
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
        "disk-usage": info_disk_usage,
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
    "log": {
        "get": log_get,
        "clear": log_clear,
        "debug": {
            "enable": log_debug_enable,
            "disable": log_debug_disable,
        }
    },
}


def get_command(cmd: str, args: list[str]):
    # NOTE: i hate python :(
    if commands.get(cmd) is None:
        log.debug('command not found')
        return None, args

    # check zero level for callable (ex: "log", ...)
    if not isinstance(commands[cmd], dict):
        return commands[cmd], args

    # check first level for args[0] (ex: "get", "clear")
    for key, value in commands[cmd].items():
        if args[0] == key:
            if not isinstance(value, dict):
                return value, args[1:]

            # check second level for args[1] (ex: "enable", "disable")
            for key, value in value.items():
                if args[1] == key:
                    if isinstance(value, dict):
                        # should never happen
                        break

                    if key == args[1]:
                        return value, args[2:]

    return None


def request_handler(req: str):
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
    @TODO ...

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
    commands_to_run: list[str] = []
    for part in req.split("\n"):
        for cmd in part.split(";"):
            commands_to_run.append(cmd.strip())

    # split command on space(s) " "
    for cmd in commands_to_run:
        args: list[str] = []

        try:
            cmd, rest_args = cmd.split(" ", 1)
            args = rest_args.split(" ")
        except ValueError:
            pass

        command, args = get_command(cmd, args)
        log.debug(
            f'running command: {cmd} {args} (valid: {command is not None})')

        return command(args) if command is not None else None
