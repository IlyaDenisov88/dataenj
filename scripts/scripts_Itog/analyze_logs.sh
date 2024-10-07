#!/bin/bash
exec 3>report.txt

echo "Общее количество запросов: ">&3
cat access.log |awk '{ count += 1 } END { print count }'>&3

echo "Количество уникальных ip-адресов: ">&3
cat access.log | awk '{ count[$1]++ } END { print length(count) }'>&3

echo "Количество запросов по методам: ">&3
cat access.log | awk '{ count[substr($6, 2)]++ } END { for (type in count) print count[type], type }'>&3

echo "Самый популяпный URL: ">&3
cat access.log | awk '{ count[$7]++ } END { for (url in count) print count[url], url }' | awk '($1 > max || NR == 1) { max = $1; max_url = $2 } END { print max, max_url }'>&3

exec 3>&-

echo "Отчет сохранен в файле report.txt" 
