FROM lazyxghost/biometric_attendance:latest
RUN apt-get update
RUN apt-get install -y python3.10 python3-pip libgl1-mesa-glx libglib2.0-0

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3.10 -m pip install --upgrade pip
RUN python3.10 -m pip install -r requirements.txt
COPY . /app
RUN export FLASK_APP=app.py
ENTRYPOINT [ "python3.10" ]
CMD ["app.py"] 
