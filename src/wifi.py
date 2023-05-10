import _thread

import config
import log
import network
import utime as time


def connect(wlan: network.WLAN, skip: bool = False):
    """..."""
    log.debug("Connecting wlan...")

    wlan.active(True)
    # wlan.config(pm=0xa11140)  # disable power-save mode
    wlan.connect(config.SSID, config.PASSWORD)

    if skip:
        return wlan

    while not wlan.isconnected():
        if not wait_for_wlan_connection(wlan):
            log.debug("...connection to wlan failed, try re-connecting...")
            wlan = connect(network.WLAN(network.STA_IF))

    log.debug("...connection established.")

    # Register this device on the server
    config.load()

    try:
        config.register_to_server(wlan.ifconfig()[0])
    except Exception as err:
        log.error(f"exception: {str(err)}")

    return wlan


def wait_for_wlan_connection(wlan: network.WLAN):
    """..."""
    count = 0
    while wlan.isconnected() is False:
        time.sleep(1)

        count += 1
        if count > 4:
            return False

    return True


def t_wifi(wlan: network.WLAN):
    """..."""
    while True:
        if not wlan.isconnected():
            wlan = connect(network.WLAN(network.STA_IF))
        else:
            utime.sleep(5)


def start():
    """..."""
    wlan = connect(network.WLAN(network.STA_IF))
    _thread.start_new_thread(t_wifi, (wlan,))
