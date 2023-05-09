import contextlib
import json

import config
import machine

U16_MAX = 65535


class Pin:
    """..."""

    def __init__(self, color: str, pin: int):
        self.current_duty = 0  # 0-100%
        self.color = color
        self.pin = pin
        self.pwm = machine.PWM(machine.Pin(pin, value=1))
        self.pwm.freq(config.PWM_FREQ)
        self.set_duty_cycle(0)

    def set_duty_cycle(self, value: int) -> None:
        """..."""
        self.pwm.duty_u16(int((1 - (value / 100)) * U16_MAX))
        self.current_duty = value

    def get_duty_cycle(self) -> int:
        """..."""
        return self.current_duty


pins: dict[str, Pin] = {}


def add(color: str, pin: int) -> None:
    """..."""
    if color in pins:
        remove(color)

    pins[color] = Pin(color, pin)


def get(color: str) -> None | Pin:
    """..."""
    return None if color not in pins else pins[color]


def remove(color: str) -> None:
    """..."""
    if color not in pins:
        return

    pins[color].set_duty_cycle(0)
    del pins[color]


def save() -> None:
    """..."""
    with open("rgbw.json", "w", encoding="utf-8") as file:
        # NOTE: tuple: color, pin, duty
        pins_data: list[tuple[str, int, int]] = []

        for color in ["r", "g", "b", "w"]:
            if color in pins:
                pin = pins[color]
                pins_data.append((pin.color, pin.pin, pin.get_duty_cycle()))

        file.write(json.dumps(pins_data))


def load() -> None:
    """..."""
    with contextlib.suppress(Exception):
        with open("rgbw.json", "r", encoding="utf-8") as file:
            # NOTE: tuple: color, pin, duty
            pins_data: list[tuple[str, int, int]] = json.load(file)

            for color in pins:
                remove(color)

            for color, gp_pin, duty in pins_data:
                pin = Pin(color, gp_pin)
                pin.set_duty_cycle(duty)
                pins[color] = pin


load()
