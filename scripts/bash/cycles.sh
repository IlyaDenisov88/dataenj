#!/bin/bash

# Циклы for

	# Пример 1: Перебор списка значений
	for color in red green blue; do 
	    echo "Color: $color" 
	done

	# Пример 2: Перебор файлов в каталоге
	for file in /hamoe/lapis/*; do 
	    echo "File: $file" 
	done

	# Пример 3: Перебор числового диапазона
	for i in {1..5}; do 
	    echo "Number: $i" 
	done

# Циклы while

	# Пример 1: Счетчик
	count=1 
	while [ $count -le 5 ]; do 
	    echo "Count: $count" 
	    count=$((count + 1)) 
	done

	# Пример 2: Чтение строк из файла 
	while IFS= read -r line; do 
	    echo "Line: $line" 
	done < /home/krokodile/dataenj_git/dataenj/dataenj_valuable/scripts/variables.sh

# Циклы until

	# Пример: Счетчик
	count=1 
	until [ $count -gt 5 ]; do 
	    echo "Count: $count" 
	    count=$((count + 1)) 
	done

# Команда break
for i in {1..10}; do 
    if [ $i -eq 5 ]; then 
        break 
    fi 
    echo "Number: $i" 
done

# Команда continue
for i in {1..10}; do 
    if [ $i -eq 5 ]; then 
        continue 
    fi 
    echo "Number: $i" 
done

# Вложенные циклы
for i in {1..3}; do
    for j in {1..3}; do
        echo "i: $i, j: $j"
    done

# Пример 1: Поиск файлов с определенным расширением и выполнение команды
for file in /path/to/directory/*.txt; do 
    echo "Processing file: $file" # Здесь можно добавить команду для обработки файла done

# Пример 2: Проверка состояния сервиса и выполнение действий
while true; do 
    if systemctl is-active --quiet my_service; then 
        echo "Service is running" 
    else 
        echo "Service is not running, restarting..." 
        systemctl restart my_service 
    fi 
    sleep 60 
done

# Пример 3: cумма всех четных чисел от 1 до введенного числа 
echo "Введите число" 
read num
sum=0
for i in $(seq 1 $num); do
    if [ $((i % 2)) -eq 0 ]; then
        sum=$((sum+i))
    fi
done
echo "Сумма всех четных чисел от 1 до введенного числа " 
echo $sum



