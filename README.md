# picow-rgbw

<!--toc:start-->
- [picow-rgbw](#picow-rgbw)
  - [Getting Started](#getting-started)
  - [Server Info](#server-info)
    - [**GET** _"/"_](#get)
    - [**GET** _"/device"_](#get-device)
    - [**POST** _"/rgbw/set_pwm"_](#post-rgbwsetpwm)
  - [TODOs](#todos)
<!--toc:end-->

Control rgbw stripes (pwm mode)

## Getting Started

> Have a look here: [https://projects.raspberrypi.org/en/projects/get-started-pico-w/1]  
> NOTE: in `./src/info.py` put in your wifi credentials (`SSID` and `PASSWORD`)

@TODO: ...

## Server Info

| Method | Pathname                                                        |
| ------ | --------------------------------------------------------------- |
| GET    | [/](#info_page)                                                 |
| GET    | [/device](#device)                                              |
| POST   | [/rgbw/set_pwm](#rgbwsetpwm)                                    |
| POST   | `/rgbw/set_pin?r=<-1/1-28>&g=<-1/1-28>&b=<-1/1-28>&w=<-1/1-28>` |
| GET    | `/rgbw/get_pins`                                                |
| GET    | `/rgbw/get_duty`                                                |
| POST   | `/server?host=<ip>`                                             |

<a id="info_page"></a>

### **GET** _"/"_

Device info page.

Example Request

```bash
curl http://192.168.178.50:80/
```

Example Response

```text
Device: picow_micropython_v0.0.1

Temp: 19.55409

Freq: 1000
Duty Range: 0-100 (%)

| Color   | Pin | Duty |
|---------|-----|------|
| [r]ed   |   0 |    0 |
| [g]reen |   1 |    0 |
| [b]lue  |   2 |    0 |
| [w]hite |   3 |    0 |
```

<a id="device"></a>

### **GET** _"/device"_

Get version information. (returns `<device>_<language>_<version>`)

Example Request

```bash
curl http://192.168.178.50:80/version
```

Example Response

```text
picow_micropython_v0.0.1
```

<a id="rgbwsetpwm"></a>

### **POST** _"/rgbw/set_pwm"_

Set the (rgbw) pwm pin duty cycle, range between 0 - 100.

Example Request

```bash
curl 'http://192.168.178.50:80/rgbw/set_pwm?r=100&g=100&b=100&w=100'
```

## TODOs

- [x] Add a temperature entry to info_page
- [x] Add handler: get duty (will return the rgbw duty cycle like this
      `100 100 100 -1` for max white) (-1 === not set)
- [x] Add handler: get pins (will return the rgbw pins like this `0 1 2 -1`)
      (-1 === not set)
- [x] Save/Load pins configuration
- [x] README: Add a routing table
- [ ] README: Add a getting started section
- [x] Adding timeout (4 seconds) to waiting for connection, else reconnect and
      wait again
- [x] Add wifi keep online thread (check every 5 seconds?)
- [ ] rename "/device" to "/version"

  - using `import _thread`
  - sleep `import utime` + `utime.sleep(5)`
  - start with `_thread.start_new_thread(func, ())`

- copy pico firmware do pico
- start thonny ide
- copy file over to the pico device
- edit config.py, add ssid and password for wifi router
- install package `micropython-contextlib`
- install package `picozero`
- run...
