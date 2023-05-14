# picow-rgbw

<!--toc:start-->
- [picow-rgbw](#picow-rgbw)
  - [Getting Started](#getting-started)
    - [Dependencies](#dependencies)
  - [Commands (Examples)](#commands-examples)
  - [TODOs](#todos)
<!--toc:end-->

Control rgbw stripes (pwm mode)

## Getting Started

> Have a look here: [https://projects.raspberrypi.org/en/projects/get-started-pico-w/1]  
> NOTE: in [src/config.py](src/config.py) put in your wifi credentials (`SSID` and `PASSWORD`)

### Dependencies

In Thonny IDE, click on Tools > "Manage Packages" and install the
following dependencies

- micropython-contextlib
- picozero

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
286720 581632

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
- [x] Adding debug log (enable and disable in config.py)
- [x] rewrite server (pure tcp server for data transfer via json data?)
      (should be debuggable via telnet client)
