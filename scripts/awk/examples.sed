# To run: "sed -f examples.sed sed_input.txt"

# Удаление строк, содержащих 'World'
/World/d

# Замена 'Hello' на 'Hi'
s/Hello/Hi/g

# Вставка текста перед строками, содержащими 'SED'
/SED/i\
This is inserted text before SED

# Вставка текста после строк, содержащих 'SED'
/SED/a\
This is inserted text after SED





# С использованием sed допишите две функции:
#1. Выводит IP-адрес, если код ответа равен 200
#2. Удаляет строку, если в ней используется метод POST (если метод иной строка выводится без изменений)

process_log() {
    echo "$1" | sed -n '
    # Поиск строк с кодом ответа 200 и вывод IP-адреса
    / 200 /p 
    ' | awk '{ print $1 }'
}

# Функция для удаления строк с POST запросами
filter_post_requests() {
    echo "$1" | sed '/POST/d'
}


