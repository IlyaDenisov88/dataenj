from kafka import KafkaProducer
import json

# Создание производителя Kafka
producer = KafkaProducer(
    bootstrap_servers='192.168.31.240:9092',
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8')  
)

# Определение сообщения в формате JSON
message = {
    'species': 'Язь',  
    'length': '30',
    'weight': '250',
    'w_l_ratio': '8.33'
}

# Отправка сообщение в нашу тему Kafka
try:
    producer.send('fish', message)
    print("Сообщение отправлено!")  # Успешная отправка сообщения
except Exception as e:
    print(f"Ошибка отправки: {e}")  # Лог ошибок отправки (на всякий случай)

# Сброс и закрытие производителя
producer.flush()
producer.close()
