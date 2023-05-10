import handler
import log
import machine
import server
import utime
import wifi
from picozero import pico_led


try:
    wifi.start()

    pico_led.on()

    sock = server.create()
    server.serve(sock, handler.request_handler)
except Exception as err:
    log.error(f"exception: {str(err)}")
finally:
    machine.reset()
    utime.sleep(1)
