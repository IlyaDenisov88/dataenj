# построчная передача данных из fish_data.csv в Kafka (табличка raw_fish)
import csv
import json
from kafka import KafkaProducer

# Параметры подключения к Kafka
bootstrap_servers = '192.168.31.240:9092'  # Замените IP адрес на адрес вашего Kafka-брокера  

# Создание продюсера Kafka
try:
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
except Exception as e:
    print(f"Ошибка при создании продюсера Kafka: {e}")
    exit(1)

# Путь к CSV файлу
csv_file_path = '/home/krokodile/dataenj_git/dataenj/kafka/fish_data.csv' #ПРОВЕРЬТЕ ПУТЬ ДО ВАШЕЙ ПАПКИ kafka

# Чтение CSV файла и отправка данных в Kafka
try:
    with open(csv_file_path, 'r', encoding='iso-8859-1') as f:
        r = csv.DictReader(f)

        # Проверка наличия всех необходимых столбцов
        required_columns = [
            'species','length','weight','w_l_ratio'

        ]
        for column in required_columns:
            if column not in r.fieldnames:
                raise ValueError(f"Отсутствует столбец '{column}' в CSV файле")

        for row in r:
            # Отправка данных в Kafka
            producer.send('fish', row)
except Exception as e:
    print(f"Ошибка при чтении CSV файла или отправке данных в Kafka: {e}")
finally:
    # Закрытие продюсера
    producer.close()
