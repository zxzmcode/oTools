from kafka import KafkaProducer

kafkaClient=KafkaProducer(bootstrap_servers='192.168.252.60:9092')

def start_producer(msg):
    kafkaClient.send('esalert',msg.encode())
    kafkaClient.flush()
    print("客户端发送完成：%s"%msg)


for i in range(10):
    mes = r'{"msgtype": "text","text": {"content": "# 你好，服务出现错误'+ str(i) + '\n***\n### 截止目前匹配到的请求数：9\n##### 错误来源: zjzwy-prod-app-loan-log-2022.09\n##### 错误详情: [traceId-] [userId-8afac0cc5aa8f06e015ae526182d7da6] 2022-09-28 16:16:37.409 [http-nio-8085-exec-16] ERROR c.d.l.s.i.LoanProductApplyServiceImpl - [setSpecificEnterprise,2862] - 企业统一信用代码为空，跳过特定企业查询\n\n"},"at": {"isAtAll": false}}'
    start_producer(mes)