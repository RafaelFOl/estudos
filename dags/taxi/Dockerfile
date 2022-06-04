FROM gcr.io/spark-operator/spark-py:v3.0.0

MAINTAINER Rafael F Oliveira

USER root:root

RUN mkdir -p /app

COPY taxi-spark.py /app/

COPY ../../k8s-config/spark/jars/ /opt/spark/jars

WORKDIR /app

USER 1001