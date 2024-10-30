from kafka import KafkaConsumer
import json
# Создание еще одного потребителя Kafka
consumer = KafkaConsumer(
    'Hello',  # Название топика
    bootstrap_servers='192.168.31.240:9092',  # Адрес ВАШЕГО сервера Kafka
    auto_offset_reset='earliest',  # Чтение сообщений с самого начала, если это первый запуск
    enable_auto_commit=True,  # Автоматическое обновление смещений (offset)
    group_id='python_reader',  # Группа потребителей
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Десериализация сообщений из JSON
)

# Чтение сообщений и вывод их в терминал
try:
    print("В ожидании сообщений...")
    for message in consumer:
        print(f"Получено сообщение из темы 'Hello': {message.value}")  # Вывод сообщения в терминал
except KeyboardInterrupt:
    print("Consumer остановлен")
finally:
    consumer.close()  # Закрытие потребителя при завершении программы

