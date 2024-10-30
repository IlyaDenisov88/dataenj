# Здесь код для получения данных с API мосбиржы за определенное время
symbol_list = [
    "SBER",
    "YNDX",
    "GAZP",
    "NVTK",
    "MTSS",
    "NKPH",
    "ALRS",
    "ENPG",
    "FGKUF",
    "GDRG",
    "IRNT",
    "KAZNO",
    "KRASN",
    "LTNA",
    "LUKO",
    "NLVK",
    "OGKB",
    "OTCP",
    "RTKM",
    "SIBR",
    "SYSTM",
    "TNRF",
    "TRNP",
    "UKRN",
    "URKN",
    "X5RT"
]


import csv
import json
from kafka import KafkaProducer
import datetime
import requests
from time import sleep
import random
import urllib.request


# Параметры подключения к Kafka
bootstrap_servers = '192.168.31.240:9092'  # Замените IP адрес на адрес вашего Kafka-брокера  

# Создание продюсера Kafka
try:
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
except Exception as e:
    print(f"Ошибка при создании продюсера Kafka: {e}")
    exit(1)

# Получение данных и отправка в kafka
try:

	columns = []
	for symb in symbol_list:
		start_date = datetime.date(2024, 1, 1)
		end_date = datetime.date.today()
		while end_date > start_date:
				# запрос
				try:
					url = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities/{symb}.json?from={str(start_date)}"
					response = urllib.request.urlopen(url)
					data = json.loads(response.read())
					sleep(random.randint(1, 3))
					print(data)
					# название колонок
					if not columns:
						columns = data['history']['columns']
					# сохранение в список cловарей
					for s in data['history']['data']:
						temp_dict = {}
						for i in range(len(data)):
							temp_dict[columns[i]] = s[i]
						print(temp_dict)
						producer.send('moex', temp_dict)
					print(f"Успех. Тикер: {symb}. Дата: {start_date}.")
				except Exception as e:
					print(f"Ошибка: {e}. Тикер: {symb}. Дата: {start_date}.")
					sleep(random.randint(5, 10))
				try:
					last_date = data['history']['data'][-1][1]
					start_date = datetime.datetime.strptime(last_date, '%Y-%m-%d').date() + datetime.timedelta(days=1)
					print(f"last_date: {last_date}, start_date: {start_date}")
				except Exception as e:
					print(f"Ошибка в датах: {e}")
					break


finally:
    # Закрытие продюсера
    producer.close()








