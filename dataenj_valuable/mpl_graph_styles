import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2)# Создаем сетку 2x2 для графиков

# Устанавливаем диапазон значений по оси X
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Рассчитываем значения Y для функций sin и cos
y_values_sin = np.sin(x_values)
y_values_cos = np.cos(x_values)

# Создаем графики для функций sin и cos
fig.set_figheight(8)
fig.set_figwidth(16)

# Синусоида
axs[0, 0].plot(x_values, y_values_sin, label='sin(x)',
         color='blue', linewidth=2, linestyle='-', marker='o',
         markersize=5, markerfacecolor='red')

# Косинусоида
axs[0, 0].plot(x_values, y_values_cos, label='cos(x)',
         color='green', linewidth=2, linestyle='--', marker='s',
         markersize=5, markerfacecolor='yellow')

axs[0, 0].set_title('Графики sin(x) и cos(x)')
axs[0, 0].legend()
axs[0, 0].grid(True)


# График функции tan может иметь очень большие значения, поэтому ограничим ось Y
# Рассчитываем значения Y для функции tan
y_values_tan = np.tan(x_values)

# Ограничиваем вертикальный размах графика
axs[0, 1].set_ylim(-10, 10)

# Создаем график для функции tan
axs[0, 1].plot(x_values, y_values_tan, label='tan(x)',
         color='purple', linestyle=':', linewidth=2)

axs[0, 1].set_title('График tan(x)')
axs[0, 1].legend()
axs[0, 1].grid(True)


# График нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
samples = np.random.normal(mean, std_dev, 10000)

# Создаем гистограмму
axs[1,0].hist(samples, bins=50, density=True, alpha=0.6, color='orange')
axs[1,0].set_title('Гистограмма нормального распределения')


# График функции tan может иметь очень большие значения, поэтому ограничим ось Y
# Рассчитываем значения Y для функции tan
y_values_ctg = np.cos(x_values)/np.sin(x_values)

# Ограничиваем вертикальный размах графика
axs[1, 1].set_ylim(-10, 10)

# Создаем график для функции tan
axs[1, 1].plot(x_values, y_values_ctg, label='ctg(x)',
         color='red', linestyle='-.', linewidth=2)

axs[1, 1].set_title('График ctg(x)')
axs[1, 1].legend()
axs[1, 1].grid(True)



# Отображаем гистограмму
plt.show()
