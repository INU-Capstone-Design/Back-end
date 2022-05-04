FROM python:3.9.10-buster

ADD . /api
WORKDIR /api

RUN gzip -d ko_w2v_model.gz

ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV TZ=Asia/Seoul
ENV CONFIG=prod HOST=0.0.0.0 PORT=5000 DATABASE=mysql
ENV PYTHONPATH "${PYTHONPATH}:/api"

RUN pip install -r requirements.txt

CMD [ "./entrypoint.sh" ]