#!/bin/bash

echo lazyghost | sudo -S docker stop app
sudo docker rm app
sudo docker run -p 8000:8000 --name app -d lazyxghost/biometric_attendance:v1.0 
sudo docker logs -f app