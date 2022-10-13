from python:3.9.7-slim
LABEL maintainer="slf@dataqin.com"
ARG ACCESS_TOKEN
ARG KAFKA_HOST
ARG KAFKA_PORT
ARG KAFKA_TOPIC
ENV ACCESS_TOKEN=${ACCESS_TOKEN} \
    KAFKA_HOST=${KAFKA_HOST} \
    KAFKA_PORT=${KAFKA_PORT} \
    KAFKA_TOPIC=${KAFKA_TOPIC}
ADD dingtalk.py /opt
RUN pip install kafka-python==2.0.2 requests==2.28.1 log21==2.3.10 -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD [ "python" , "/opt/dingtalk.py"]

