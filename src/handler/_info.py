import os

from picozero import pico_temp_sensor


def info_temp(_args: list[str]) -> str:
    """..."""
    return f"{pico_temp_sensor.temp}"


def info_disk_usage(_args: list[str]) -> str:
    """..."""
    disk = os.statvfs("/")

    block_size = disk[0]
    total_blocks = disk[2]
    free_blocks = disk[3]

    used = (block_size * total_blocks) - (block_size * free_blocks)
    free = block_size * free_blocks

    return f"{used} {free}"
