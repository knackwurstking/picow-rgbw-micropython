import contextlib
import json

import machine

initial_pin_value = 1
freq = 1000
u16_max = 65535


class Pin:
    def __init__(self, color: str, pin: int):
        self.current_duty = 0  # 0-100%
        self.color = color
        self.pin = pin
        self.pwm = machine.PWM(machine.Pin(pin, value=1))
        self.pwm.freq(freq)
        self.set_duty_cycle(0)

    def set_duty_cycle(self, value: int):
        self.pwm.duty_u16(int((1 - (value/100)) * u16_max))
        self.current_duty = value

    def get_duty_cycle(self):
        return self.current_duty


pins: dict[str, Pin] = {}


def add(color: str, pin: int):
    if color in pins:
        remove(color)

    pins[color] = Pin(color, pin)


def get(color):
    return None if color not in pins else pins[color]


def remove(color: str):
    if color not in pins:
        return

    pins[color].set_duty_cycle(0)
    del pins[color]


def save():
    with open("config.json", "w") as c:
        # NOTE: tuple: color, pin, duty
        _pins: list[tuple[str, int, int]] = []

        for color in ["r", "g", "b", "w"]:
            if color in pins:
                pin = pins[color]
                _pins.append((pin.color, pin.pin, pin.get_duty_cycle()))

        c.write(json.dumps(_pins))


def load():
    with contextlib.suppress(Exception):
        with open("config.json", "r") as c:
            # NOTE: tuple: color, pin, duty
            _pins: list[tuple[str, int, int]] = json.load(c)

            for color in pins:
                remove(color)

            for color, pin, duty in _pins:
                pin = Pin(color, pin)
                pin.set_duty_cycle(duty)
                pins[color] = pin


load()
