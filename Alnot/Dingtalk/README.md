# Dingtalk

&emsp; 该项目主要为了是用于ElastAlert告警的方案。适用于内网无法直接访问公网的环境下。

&emsp; 个人使用该项目的环境是内网只能访问政务专网，但政务专网不能访问政务公网，而政务公网能访问政务专网的特殊网络环境下。

### 使用方式

* docker

&emsp; docker使用该脚本，可以直接执行以下命令。

&emsp; KAFKA_PORT该环境变量如不是提供，则提供Kafka的默认端口9092。

```shell
cd {path}/kafka_to_dingtalk
docker build -t kafka_to_dingtalk:v0.1 .
docker run -itd -e ACCESS_TOKEN=${你的钉钉机器人access_token} \
-e KAFKA_HOST=${你的kafka的IP} -e KAFKA_PORT=${你的kafka的端口} -e KAFKA_TOPIC=${你的kafka的主题} \
--name esalert kafka_to_dingtalk:v0.1 
```

* Python

&emsp; 如果直接使用Python跑该脚本，Python应该保证在python3(脚本编写是使用的3.9.7)。

```shell
cd {path}/kafka_to_dingtalk
pip install -r requirements.txt
nohup python3 dingtalk.py &
```
