# picow-rgbw

<!--toc:start-->
- [picow-rgbw](#picow-rgbw)
  - [Getting Started](#getting-started)
  - [Server Info](#server-info)
    - [**GET** _"/"_](#get)
    - [**GET** _"/device"_](#get-device)
    - [**GET** _"/server"_](#get-server)
    - [**POST** _"/server"_](#post-server)
    - [**POST** _"/rgbw/set_pin"_](#post-rgbwsetpin)
    - [**POST** _"/rgbw/set_pwm"_](#post-rgbwsetpwm)
    - [**GET** _"/rgbw/get_pins"_](#get-rgbwgetpins)
    - [**GET** _"/rgbw/get_duty"_](#get-rgbwgetduty)
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

## Server Info

| Method | Pathname                           |
| ------ | ---------------------------------- |
| GET    | [/](#info_page)                    |
| GET    | [/device](#get-device)             |
| GET    | [/server](#get-server)             |
| POST   | [/server](#post-server)            |

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

### **GET** _"/server"_

Get web server address in use.

Example Request

```bash
curl http://192.168.178.50:80/server
```

Example Response

```text
http://192.168.178.20:50833
```

### **POST** _"/server"_

Configure the ([picow-rgbw-web](https://github.com/knackwurstking/picow-rgbw-web.git)) server to use for registration.
The pico device will register itself on the web server

Example Request

```bash
curl 'http://192.168.178.50:80/server?host=192.168.178.50'
```

## TODOs

- [ ] README: Add a getting started section
- [ ] ~Rename "/device" to "/version"~
- [x] Adding debug log (enable and disable in config.py)
- [ ] rewrite server (pure tcp server for data transfer via json data?)
      (should be debuggable via telnet client)
