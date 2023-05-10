# FROM ubuntu22.04:latest
# RUN apt-get update
# RUN apt-get install -y python3.10 python3-pip libgl1-mesa-glx libglib2.0-0
# RUN python3.10 -m pip install --upgrade pip

FROM lazyxghost/biometric_attendance:latest

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3.10 -m pip install -r requirements.txt
COPY . /app

RUN export FLASK_APP=app.py
EXPOSE 8000
ENTRYPOINT [ "python3.10" ]
CMD ["-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]

