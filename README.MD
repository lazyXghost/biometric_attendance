> export FLASK_APP=app
> export FLASK_ENV=development
> flask run
> flask shell


> docker proxy
``
location - /etc/systemd/system/docker.service.d
1. file - http-proxy.conf
[Service]
Environment="HTTP_PROXY=http://proxyserveraddress:proxyport"
2. file - https-proxy.conf
[Service]
Environment="HTTPS_PROXY=https://proxyserveraddress:proxyport"

sudo systemctl daemon-reload
sudo systemctl restart docker
``

> docker commands
``
sudo docker login -u lazyxghost
sudo docker image prune
sudo docker ps -a
sudo docker rmi image_name:image_version
sudo docker images -a
sudo docker push lazyxghost/biometric_attendance
sudo docker tag biometric_attendance lazyxghost/biometric_attendance
sudo docker rm testcontainer
sudo docker run --name testcontainer bio_att:running
``
