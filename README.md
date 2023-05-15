# picow-rgbw-micropython

<!--toc:start-->
- [picow-rgbw-micropython](#picow-rgbw-micropython)
  - [(Thonny) Dependencies](#thonny-dependencies)
  - [Getting Started](#getting-started)
  - [Commands (Examples)](#commands-examples)
  - [TODOs](#todos)
<!--toc:end-->

Control rgbw stripes (pwm mode)

## (Thonny) Dependencies

In Thonny IDE, click on Tools > "Manage Packages" and install the
following dependencies

- micropython-contextlib
- picozero

## Getting Started

> Have a look here: [https://projects.raspberrypi.org/en/projects/get-started-pico-w/1]  
> NOTE: in [src/config.py](src/config.py) put in your wifi credentials (`SSID` and `PASSWORD`)

@TODO: ...

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

- [ ] add motion sensor for auto control lights (question: how many threads
      can i start on a picow?)
