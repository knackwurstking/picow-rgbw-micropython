import config
import handler
import log
import machine
import rgbw
import server
import utime as time
import wifi
from picozero import pico_led


try:
    rgbw.load()
    config.load()

    wifi.start()

    pico_led.on()

    sock = server.create()
    server.serve(sock, handler.request_handler)
except Exception as err:
    log.error(f"exception: {str(err)}")
finally:
    machine.reset()
    time.sleep(1)
