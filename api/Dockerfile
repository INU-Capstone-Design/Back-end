FROM python:3.9.10-buster

ADD . /api
WORKDIR /api

RUN pip install -r requirements.txt

ENV CONFIG=prod HOST=0.0.0.0 PORT=80 DATABASE=mysql

CMD [ "python3", "-u", "app.py" ]