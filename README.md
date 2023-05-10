# picow-rgbw

<!--toc:start-->
- [picow-rgbw](#picow-rgbw)
  - [Getting Started](#getting-started)
  - [Commands (Examples)](#commands-examples)
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

## Commands (Examples)

```text
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

Get disk usage info (`<used> <free>`)
>>> info disk-usage

Get device logs
>>> log get
[DEBUG] ...
[ INFO] ...
...

Enable/Disable debugging
>>> log debug enable
>>> log debug disable

Clear all device logs
>>> log clear

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
```

## TODOs

- [ ] README: Add a getting started section
- [ ] ~Rename "/device" to "/version"~
- [x] Adding debug log (enable and disable in config.py)
- [ ] rewrite server (pure tcp server for data transfer via json data?)
      (should be debuggable via telnet client)
