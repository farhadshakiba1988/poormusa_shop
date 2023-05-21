FROM python:slim-buster
ENV PYTHONUNBUFFRED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt