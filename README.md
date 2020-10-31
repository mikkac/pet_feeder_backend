# PetFeeder Backend 

## Introduction
This repo contains backend part of PetFeeder application. It's project whose purpose is to create DYI feeder controlled remotely.

## Docker
This will build docker image and run backend server from docker container

#### Build
This will create image tagged with `pet_feeder_backend`, only necessary if you haven't build this image before

 ```
 docker build -t pet_feeder_backend:latest .
 ```

 #### Run
This will start docker container with server exposed on selected PORT

 ```
 docker run -p PORT:5000 pet_feeder_backend
 ```

You can also pass optional arguments listed in [run section](#run) e.g.:

```
docker run -p 5000:5000 pet_feeder_backend --fake_servo=true
```

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

## <a name="run"></a>Run
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
* RaspberryPi with servomechanism connected, e.g.
```bash
python3 python/server.py --portions_limit=8 --gpio=11 --port=3333
```

* Debug environment without servo connected, e.g.
```bash
python3 python/server.py --portions_limit=8 --port=3333 --fake_servo=true
```
