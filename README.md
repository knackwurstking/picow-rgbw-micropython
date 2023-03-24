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
> NOTE: in `./src/info.py` put in your wifi credentials  

@TODO: ...

## Routing

| Method | Pathname | Description |
|--------|----------|-------------|
| GET    | `/` | Get info\_page (text/text) |
| GET    | `/device` | Get application info and version |
| POST   | `/set_rgbw_pwm?r=<0-100>&g=<0-100>&b=<0-100>&w=<0-100>` | Set duty cycle for pins (rgbw) |
| POST   | `/set_rgbw_pin?r=<1-28>&g=<1-28>&b=<1-28>&w=<1-28>` | Set pins in use for rgbw |

## TODOs

- [x] Add a temperature entry to info\_page
- [x] README: Add a routing table
- [ ] README: Add a getting started section
