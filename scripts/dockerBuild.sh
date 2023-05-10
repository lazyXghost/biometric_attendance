#!/bin/bash

echo lazyghost | sudo -S docker build -t lazyxghost/biometric_attendance:v1.0 .
sudo docker image prune -f