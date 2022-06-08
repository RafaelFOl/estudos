FROM gcr.io/spark-operator/spark-py:v3.0.0

MAINTAINER Rafael F Oliveira

USER root:root

RUN mkdir -p /app

COPY taxispark.py /app/
RUN ls
COPY ./jars/ /opt/spark/jars/

WORKDIR /app

USER 1001