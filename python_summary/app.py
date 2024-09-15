import matplotlib.pyplot as plt

def read_sales_data(file_path):
	'''Считывает данные из файла и переводит в список строк'''
	with open (file_path, "r") as file:
		sales_list = file.readlines()
	return sales_list
	
def total_sales_per_product(sales_list):
	'''Из списка строк рассчитывает общую сумму продаж каждого товара, возвращает словарь'''
	total_money_per_product = {}
	for line in sales_list:
		name = line.split(', ')[0]
		sum_sold = int(line.split(', ')[1]) * int(line.split(', ')[2])
		if name in total_money_per_product.keys():
			total_money_per_product[name] += sum_sold
		else:
			total_money_per_product[name] = sum_sold
	return total_money_per_product
	
def sales_over_time(sales_list):
	'''Из списка строк рассчитывает общую сумму продаж в каждый день, возвращает словарь'''
	total_money_per_date = {}
	for line in sales_list:
		date = line.split(', ')[3]
		date = date[:-1] #убрать символ переноса строки в конце
		sum_sold = int(line.split(', ')[1]) * int(line.split(', ')[2])
		if date in total_money_per_date.keys():
			total_money_per_date[date] += sum_sold
		else:
			total_money_per_date[date] = sum_sold
	return total_money_per_date
	
	
try:
	# Вызов функций
	sales_list = read_sales_data('sales.txt')

	total_per_product = total_sales_per_product(sales_list)

	total_per_date = sales_over_time(sales_list)

	# Рассчет продукта и даты максимальной прибыли
	top_product = max(total_per_product, key=total_per_product.get)
	top_date = max(total_per_date, key=total_per_date.get)
	print(f'Самый прибыльный продукт: {top_product}, общая стоимость продаж: {total_per_product[top_product]}')
	print(f'Самый прибыльный день: {top_date}, общая стоимость продаж: {total_per_date[top_date]}')
	
	# построение графиков
	x1 = sorted(total_per_product.keys(), key=total_per_product.get)
	y1 = [total_per_product[i] for i in x1]

	x2 = sorted(total_per_date.keys())# отсортировали время
	y2 = [total_per_date[i] for i in x2]

	fig, axs = plt.subplots(1, 2)
	fig.set_figheight(5)
	fig.set_figwidth(15)
	axs[0].barh(x1, y1)
	axs[0].set_title('Выручка с товаров')
	axs[1].plot(x2, y2, marker='s')
	axs[1].set_title('Выручка по дате')
	plt.show()

except Exception as e:
	print(f'Exception {e} occured')
	
	



