FROM gcr.io/spark-operator/spark-py:v3.0.0

MAINTAINER Rafael F Oliveira

USER root:root

RUN mkdir -p /app

COPY taxispark.py /app/ 

COPY ./jars/ /opt/spark/jars/

WORKDIR /app

RUN chmod 777 /app

RUN chmod 777 /app/taxispark.py

RUN pip install ocean-spark-airflow-provider
 

USER 1001