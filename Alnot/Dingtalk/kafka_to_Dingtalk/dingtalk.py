# -*- coding: utf-8 -*-
import json
import requests
import os
import time
import log21
from kafka import KafkaConsumer

access_token = os.environ.get("ACCESS_TOKEN")
kafka_host = os.environ.get("KAFKA_HOST")
kafka_port = os.environ.get("KAFKA_PORT", "9092")
kafka_topic = os.environ.get("KAFKA_TOPIC")

def dingtalk_robot(text):
    url = "https://oapi.dingtalk.com/robot/send?access_token=" + access_token

    headers = {'Content-Type': 'application/json'}

    data_dict = {
        "msgtype": "markdown",
        "markdown": {
            "title": "日志告警",
            "text": text
        }
    }

    json_data = json.dumps(data_dict)
    response = requests.post(url, data=json_data, headers=headers)
    print(response.text)  # {"errcode":0,"errmsg":"ok"}


def test_to_json(message):
    data = json.loads(message, strict=False)
    return data.get('text').get('content')


def kafka_to_dingtalk():
    if kafka_port == '':
        bootstrap_server = '{}:{}'.format(kafka_host,'9092')
    else:
        bootstrap_server = '{}:{}'.format(kafka_host, kafka_port)
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers=bootstrap_server,
        auto_offset_reset='latest',
        api_version=(0, 10, 2)
    )
    log21.print(type(consumer))
    for msg in consumer:
        dingtalk_massage = test_to_json(msg.value.decode())
        time.sleep(4)
        dingtalk_robot(dingtalk_massage)


if __name__ == '__main__':
    if access_token == '':
        log21.print(log21.get_color('#FF0000') + '未提供钉钉机器人ACCESS_TOKEN' )
    if kafka_host == '':
        log21.print(log21.get_color('#FF0000') + '未配置Kafka的环境变量KAFKA_HOST' )
    if kafka_host == '':
        log21.print(log21.get_color('#FF0000') + '未配置Kafka的环境变量KAFKA_TOPIC' )
    kafka_to_dingtalk()
