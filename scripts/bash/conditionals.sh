#!/bin/bash

# if-elif-else statement

number=7
if [ $number -gt 10 ]; then
    echo "Number is greater than 10"
elif [ $number -eq 7 ]; then
    echo "Number is equal to 7"
else
    echo "Number is less than or equal to 10 but not 7"
fi

# case statement

color="red"
case $color in
    "red")
        echo "Color is red" ;;
    "blue")
        echo "Color is blue" ;;
    "green")
        echo "Color is green" ;;
    *)
        echo "Color is unknown" ;;
esac

#Логические операторы
a=6
if [ $a -gt 0 ] && [ $a -lt 10 ]; then
    echo "a is between 0 and 10"
fi

#Использование if с командами
mkdir test
if cd test; then
    echo "Directory exists"
else
    echo "Directory does not exist"
fi


# Команда ls /some/directory выполнится, и если она завершится успешно (возвращает статус 0), выполнится блок команд после then. В противном случае выполнится блок команд после else.


# Пример использования case для обработки аргументов:

echo "Enter a choice (start/stop/restart):"
read choice

case $choice in
    "start")
        echo "Starting the service..."
        # команды для старта сервиса
        ;;
    "stop")
        echo "Stopping the service..."
        # команды для остановки сервиса
        ;;
    "restart")
        echo "Restarting the service..."
        # команды для перезапуска сервиса
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

workdir= pwd
rmdir "$workdir/test"



