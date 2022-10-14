from python:3.7.13-slim
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
RUN pip install kafka-python requests log21-i https://pypi.tuna.tsinghua.edu.cn/simple
CMD [ "python" , "/opt/dingtalk.py"]

