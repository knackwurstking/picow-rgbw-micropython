# picow-rgbw

<!--toc:start-->

- [picow-rgbw](#picow-rgbw)
  - [Getting Started](#getting-started)
  - [Routing](#routing)
  - [TODOs](#todos)
  <!--toc:end-->

Control rgbw stripes (pwm mode)

## Getting Started

> Have a look here: [https://projects.raspberrypi.org/en/projects/get-started-pico-w/1]  
> NOTE: in `./src/info.py` put in your wifi credentials (`SSID` and `PASSWORD`)

@TODO: ...

## Routing

| Method | Pathname                                                        | Description                                                |
| ------ | --------------------------------------------------------------- | ---------------------------------------------------------- |
| GET    | `/`                                                             | Get info_page (text/text)                                  |
| GET    | `/device`                                                       | Get application info and version                           |
| POST   | `/rgbw/set_pwm?r=<0-100>&g=<0-100>&b=<0-100>&w=<0-100>`         | Set duty cycle for pins (rgbw)                             |
| POST   | `/rgbw/set_pin?r=<-1/1-28>&g=<-1/1-28>&b=<-1/1-28>&w=<-1/1-28>` | Set rgbw pins (-1 to remove)                               |
| GET    | `/rgbw/get_pins`                                                | get rgbw pins (-1 if pin not set)                          |
| GET    | `/rgbw/get_duty`                                                | get the current duty (-1 if pin not set) for rgbw (0-100%) |

## TODOs

- [x] Add a temperature entry to info_page
- [x] Add handler: get duty (will return the rgbw duty cycle like this
      `100 100 100 -1` for max white) (-1 === not set)
- [x] Add handler: get pins (will return the rgbw pins like this `0 1 2 -1`)
      (-1 === not set)
- [x] Save/Load pins configuration
- [x] README: Add a routing table
- [ ] README: Add a getting started section
- [ ] Adding timout (4 seconds) to waiting for connection, else reconnect and
      wait again
- [ ] Add wifi keep online thread (check every 5 seconds?)
  - using `import _thread`
  - sleep `import utime` + `utime.sleep(5)`
  - start with `_thread.start_new_thread(func, ())`
