# picow-rgbw

<!--toc:start-->
- [picow-rgbw](#picow-rgbw)
  - [Getting Started](#getting-started)
  - [Server Info](#server-info)
    - [**GET** _"/"_](#get)
    - [**GET** _"/device"_](#get-device)
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
> NOTE: in [/src/config.py](src/config.py) put in your wifi credentials (`SSID` and `PASSWORD`)

@TODO: ...

- copy pico firmware do pico
- start thonny ide
- copy file over to the pico device
- edit config.py, add ssid and password for wifi router
- install package `micropython-contextlib`
- install package `picozero`
- run...

## Server Info

| Method | Pathname                       |
| ------ | ------------------------------ |
| GET    | [/](#info_page)                |
| GET    | [/device](#get-device)             |
| POST   | [/server](#post-server)             |
| POST   | [/rgbw/set_pin](#post-rgbwsetpin)   |
| POST   | [/rgbw/set_pwm](#post-rgbwsetpwm)   |
| GET    | [/rgbw/get_pins](#get-rgbwgetpins) |
| GET    | [/rgbw/get_duty](#get-rgbwgetduty) |

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

### **POST** _"/server"_

Configure the ([picow-rgbw-web](https://github.com/knackwurstking/picow-rgbw-web.git)) server to use for registration.
The pico device will register itself on the web server

Example Request

```bash
curl 'http://192.168.178.50:80/server?host=192.168.178.50'
```

### **POST** _"/rgbw/set_pin"_

Set gpio pin to use as rgbw, range between 0-28.

Example Request

```bash
curl 'http://192.168.178.50:80/rgbw/set_pwm?r=0&g=1&b=2&w=3'
```

### **POST** _"/rgbw/set_pwm"_

Set the (rgbw) pwm pin duty cycle, range between 0-100.

Example Request

```bash
curl 'http://192.168.178.50:80/rgbw/set_pwm?r=100&g=100&b=100&w=100'
```

### **GET** _"/rgbw/get_pins"_

Get gpio pins in use for rgbw, Range between 0-28.

Example Request

```bash
curl https://192.168.178.50:80/rgbw/get_pins
```

Example Response

```text
0 1 2 3
```

### **GET** _"/rgbw/get_duty"_

Get the current rgbw duty cycle, range between 0-100.

Example Request

```bash
curl https://192.168.178.50:80/rgbw/get_pins
```

Example Response

```text
0 1 2 3
```

## TODOs

- [ ] README: Add a getting started section
- [ ] rename "/device" to "/version"
