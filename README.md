# PetFeeder Backend 

## Introduction
This repo contains backend part of PetFeeder application. It's part of project which purpose is to create DYI feeder controlled remotely.

## Requirements
* python 3.0+ with `venv` module
* pip

## Install

```bash
git clone https://github.com/mikkac/pet_feeder_backend
cd pet_feeder_backend
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
```

## Run
Main module is located in `python/server.py`. It can be run with few options:
```bash
usage: server.py [-h] [--portions_limit PORTIONS_LIMIT] [--gpio GPIO]
                 [--port PORT] [--fake_servo FAKE_SERVO]

optional arguments:
  -h, --help            show this help message and exit
  --portions_limit PORTIONS_LIMIT
                        Portions limit in the feeder
  --gpio GPIO           Number of GPIO used by Servomechanism
  --port PORT           Serving port
  --fake_servo FAKE_SERVO
                        Whether FakeServo shall be used ('true' if yes)
```
Application is prepared to be run in two environments:
* RaspberryPi with servomechanism connected:
```bash
python3 python/server.py --portions_limit=8 --gpio=11 --port=3333
```

* Debug environment without servo connected:
```bash
python3 python/server.py --portions_limit=8 --port=3333 --fake_servo=true
```
