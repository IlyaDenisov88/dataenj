from kafka import KafkaConsumer
import json
import psycopg2
import signal
import sys

# Параметры подключения к Kafka
bootstrap_servers = '192.168.31.240:9092'
topic = 'fish'  # Название темы, из которой читаем сообщения!
group_id = 'postgresql_reader'

# Параметры подключения к PostgreSQL
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'
db_user = 'ilya'
db_password = 'Ferrumvera'

# Создание потребителя Kafka
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    group_id=group_id,
    auto_offset_reset='earliest',  # Начинать чтение самого первого сообщения темы
    enable_auto_commit=True,  # Автоматически фиксировать смещения (offset'ы)
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

# Функция для обработки прерывания
def signal_handler(sig, frame):
    print('Нажаты Ctrl+C! Передача прервана')
    consumer.close()
    conn.close()
    sys.exit(0)

# Установка обработчика прерывания
signal.signal(signal.SIGINT, signal_handler)

# Функция для вставки данных в PostgreSQL
def insert_into_postgres(data):
    try:
        with conn.cursor() as cursor:  
            insert_query = """
            INSERT INTO fish_postgres (species, length, weight, w_l_ratio)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                data['species'], data['length'], data['weight'], data['w_l_ratio']
            ))
            conn.commit()
            return True  # Возвращаем True, если вставка успешна
    except Exception as e:
        print(f"Error inserting data: {e}")
        return False  # Возвращаем False, если возникла ошибка

# Чтение данных из Kafka и запись в PostgreSQL
record_count = 0  # Счетчик успешно вставленных записей

try:
    for message in consumer:
        data = message.value
        if insert_into_postgres(data):
            record_count += 1  # счетчик для справки
            print(f"Вставляем в PG сообщение: {data}")
except KeyboardInterrupt:
    signal_handler(None, None)
except Exception as e:
    print(f"Error consuming messages: {e}")
finally:
    consumer.close()
    conn.close()
    print(f"Успешно обработано {record_count} записей.")  # Выводим общее количество вставленных записей (показывает после остановки кода)

