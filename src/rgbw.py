import machine

initial_pin_value = 1
freq = 1000
u16_max = 65535

rgbw: dict[str, tuple[int, machine.PWM]] = {}


def add(color: str, pin: int):
    if color in rgbw:
        remove(color, pin)

    rgbw[color] = (pin, machine.PWM(machine.Pin(pin, value=1)))
    rgbw[color][1].freq(freq)
    rgbw[color][1].duty_u16(u16_max)


def remove(color: str, pin: int):
    if color not in rgbw:
        return

    if rgbw[color][0] == pin:
        rgbw[color][1].duty_u16(u16_max)
        del rgbw[color]


def set(color: str, value: int):
    if color not in rgbw:
        return

    rgbw[color][1].duty_u16(int((1 - (value/100)) * u16_max))


def get(color: str):
    return None if color not in rgbw else rgbw[color]
