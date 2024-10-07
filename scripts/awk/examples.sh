#!/bin/bash
# Примеры использования AWK
# Во всех командах используется пайп (везде вывод команды echo передается в команду awk и там уже изменяется дальше)

# Простой вывод полей (поле тут это как столик в БД, запись - строка):
echo -e "John 28\nJane 32\nTom 25\nAlice 29" | awk '{ print $1 }'

# Вывод строк с определенным шаблоном(вывести всю строку, с условием, что второе поле > 30):
echo -e "John 28\nJane 32\nTom 25\nAlice 29" | awk '$2 > 30 { print $0 }'

# Использование переменных и арифметических операций(посчитать сумму возрастов):
echo -e "John 28\nJane 32\nTom 25\nAlice 29" | awk '{ sum += $2 } END { print sum }'

# Форматированный вывод с printf(форматируем красивый вывод printf):
echo -e "John 28\nJane 32\nTom 25\nAlice 29" | awk '{ printf "%s is %d years old\n", $1, $2 }'

# Использование массивов(получить уникаьлные слова в массив count, получить слова и их число раз):
echo -e "apple\nbanana\napple\norange\nbanana\nbanana" | awk '{ count[$1]++ } END { for (word in count) print word, count[word] }'





