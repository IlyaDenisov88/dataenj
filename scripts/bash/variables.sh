#!/bin/bash

name="John" 
age=30 
greeting="Hello, $name"


echo $name 
echo $age

single_quote='This is $name' 
echo $single_quote # Выведет: This is $name

double_quote="Hello, $name" 
echo $double_quote # Выведет: Hello, John

local_var="I am local" 
echo $local_var

export global_var="I am global" 
bash -c 'echo $global_var' # Выведет: I am global

echo "Enter your name:" 
read user_name 
echo "Hello, $user_name"


# Специальные переменные
#	'''
#	$0 : Имя текущего скрипта.
#	$1, $2, ... : Параметры, переданные в скрипт.
#	$# : Количество аргументов, переданных в скрипт.
#	$@ : Все аргументы, переданные в скрипт.
#	$? : Статус завершения последней выполненной команды.
#	$$ : PID текущего процесса.
#	$! : PID последнего запущенного в фоне процесса.
#	'''
	
echo "Script name: $0" 
echo "First argument: $1" 
echo "Number of arguments: $#"

# Операции с переменными
	a=10 
	b=5 

	# Использование let 
	let sum=a+b 
	echo $sum # Выведет: 15 

	# Использование $(( )) 
	sum=$((a + b)) 
	echo $sum # Выведет: 15 

	# Использование expr 
	sum=$(expr $a + $b) 
	echo $sum # Выведет: 15

# Строковые операции
	# Конкатенация строк 
	str1="Hello" 
	str2="World" 
	greeting="$str1, $str2!" 
	echo $greeting # Выведет: Hello, World! 

	# Длина строки 
	str="Hello, World!" 
	echo ${#str} # Выведет: 13

# Примеры использования переменных в скриптах
	# Объявление переменных 
	name="Alice" 
	age=25 

	# Вывод значений переменных 
	echo "Name: $name" 
	echo "Age: $age" 

	# Арифметическая операция 
	year_of_birth=$((2024 - age)) 
	echo "Year of birth: $year_of_birth" 

	# Чтение значения переменной из ввода 
	echo "Enter your favorite color:" 
	read color 
	echo "Your favorite color is $color" 

	# Использование специальной переменной 
	echo "Script name: $0"


