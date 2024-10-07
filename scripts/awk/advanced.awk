# Чтобы запустить: "awk -f script.awk"

# Пользовательские функции(для повторно используемого кода):
function square(x) {
    return x * x
}

BEGIN {
    print "Square of 5 is", square(5)
}

# Управляющие структуры(Поддержка if-else, while, for и других управляющих структур):
	#Пример 1:
	
	function square(x) { 
	    return x * x 
	} 

	BEGIN { 
	    if (ARGC != 2){
		print "Передано неверное количество аргументов"
		print "Используйте следующий шаблон:"
		print "awk -f script.awk number"
	    }
	    else{
		print "Число", ARGV[1], "в квадрате =",square(ARGV[1]) 
	    }
	    
	}
	# Пример 2: 
	
	{
	    for (i = 1; i <= NF; i++) {
		print "Строка", NR, "слово под номером", i, "это", $i
	    }
	}
	
	# Пример 3:
	
	BEGIN {
	    if (ARGC != 2) {
		print "Передано неверное количество аргументов"
		print "Используйте следующий шаблон:"
		print "awk -f script.awk number"
		exit 1
	    }
	    N = ARGV[1]
	    i = 1
	    while (i <= N) {
		print i
		i++
	    }
	}

# Работа с несколькими файлами:
awk 'FNR == 1 { print "Processing " FILENAME } { print }' file1.txt file2.txt





