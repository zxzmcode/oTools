# -*- coding: utf-8 -*-
import json
import requests
import os

# from logging42 import logger
from kafka import KafkaConsumer

access_token = os.environ.get("ACCESS_TOKEN", "e91109022bbfa6d483a130c24d3b350e9d1766a511a592b54213f5b671e9bc41")
kafka_host = os.environ.get("KAFKA_HOST",'192.168.252.60')
kafka_port = os.environ.get("KAFKA_PORT", 9200)
kafka_topic = os.environ.get("KAFKA_TOPIC","esalert")

kafka = '{}:{}'.format(kafka_host, kafka_port)

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
    data = json.load(message)
    content = data.get('text').get('content')
    return content


def kafka_to_dingtalk():
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers=['192.168.252.60:9092'], 
        auto_offset_reset='earliest', 
        api_version=(0, 10, 2)
    )
    for msg in consumer:
        dingtalk_massage=test_to_json(msg.value.decode())
        dingtalk_robot(dingtalk_massage)

kafka_to_dingtalk()


# if __name__ == '__main__':
#     kafka_to_dingtalk()


# with open('E:\log.json', encoding='utf-8') as message:
#     data = json.load(message)
#     content = data.get('text').get('content')
#     dingtalk_robot(content)
