FROM python:latest

MAINTAINER admas@supersqa.com

RUN apt-get update && apt-get -y install vim

RUN mkdir /automation

COPY ./ssqaapitest /automation/ssqaapitest
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install