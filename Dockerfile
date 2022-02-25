FROM ubuntu:latest
MAINTAINER Eden Attenborough "eddie.atten.ea29@gmail.com"
RUN apt-get update -y
RUN apt-get install -y autossh python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["tunnel.py"]
