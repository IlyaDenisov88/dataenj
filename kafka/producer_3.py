from kafka import KafkaProducer
import json

# Создание продюсера Kafka
producer = KafkaProducer(
    bootstrap_servers='192.168.31.240:9092',
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8')  
)

# Создание сообщения
message = {
    'message': 'Привет, самый лучший студент курса "Data Engineer с нуля до junior!"'  
}

# Отправка сообщение в тему Kafka
try:
    producer.send('Hello', message)  # Отправляем сообщение в тему 'Hello'
    print("Сообщение успешно отправлено!")  # Успешная отправка сообщения
except Exception as e:
    print(f"При отправке возникла ошибка: {e}")  # Лог ошибок 


producer.flush()
producer.close()

