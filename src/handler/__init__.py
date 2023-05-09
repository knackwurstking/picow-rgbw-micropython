def request_handler(req: bytes):
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

    # TODO: read data from request (json unmarshal)
    # data format: `{ command: str, options: dict }`

    # TODO: run command with options

    # TODO: return json data or close on empty response

    pass
