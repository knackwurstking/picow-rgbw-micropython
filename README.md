# picow-rgbw

<!--toc:start-->
- [picow-rgbw](#picow-rgbw)
  - [Getting Started](#getting-started)
  - [TODOs](#todos)
<!--toc:end-->

Control rgbw stripes (pwm mode)

## Getting Started

> Have a look here: [https://projects.raspberrypi.org/en/projects/get-started-pico-w/1]  
> NOTE: in [src/config.py](src/config.py) put in your wifi credentials (`SSID` and `PASSWORD`)

@TODO: ...

- copy pico firmware do pico
- start thonny ide
- copy file over to the pico device
- edit config.py, add ssid and password for wifi router
- install package `micropython-contextlib`
- install package `picozero`
- run...

## TODOs

- [ ] README: Add a getting started section
- [ ] ~Rename "/device" to "/version"~
- [x] Adding debug log (enable and disable in config.py)
- [ ] rewrite server (pure tcp server for data transfer via json data?)
      (should be debuggable via telnet client)
