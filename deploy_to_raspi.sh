#!/bin/bash

rsync -avhe ssh python pi@$1:feeder_backend
rsync -avhe ssh requirements.txt pi@$1:feeder_backend
