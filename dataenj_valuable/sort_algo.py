## Линейная сортировка
## Сложность - по времени O(n) в среднем, по памяти О(1)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Пример использования:
arr = [5, 3, 7, 1, 9]
target = 7
result = linear_search(arr, target)
print(f'Элемент найден на индексе: {result}' if result != -1 else 'Элемент не найден')



## Бинарный поиск - сложность по времени О(log n) - в среднем, по памяти - О(1) для итеративной и O(n*logn) для рекурсивной (из-за стека вызовов)
# Итеративная реализация
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Пример использования:
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
print(f'Элемент найден на индексе: {result}' if result != -1 else 'Элемент не найден')

## Рекурсивная реализация
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Пример использования:
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f'Элемент найден на индексе: {result}' if result != -1 else 'Элемент не найден')
# ДЛЯ БИН ПОИСКА МАССИВ ДОЛЖЕН БЫТЬ ОТСОРТИРОВАН!! (минус)



## Сортировка пузырьком - сложность по времени О(n^2), по памяти - О(1) - не требует доп памяти, кроме константного значения переменных для обменов.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для отслеживания изменений на текущем проходе
        swapped = False
        # Проход по массиву до n-i-1, так как последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Меняем элементы местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break

# Пример использования:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Отсортированный массив:", arr)



## Сортировка вставками - как пузырьковая, только обратно (Элемент сравнивается с уже отсортированными элементами, сдвигая их вправо, если они больше текущего элемента.) 
## сложность по времени O(n^2), по памяти - О(1)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Сдвигаем элементы arr[0..i-1], которые больше key, на одну позицию вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Пример использования:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Отсортированный массив:", arr)


## Быстрая сортировка (Quick Sort) - Временная сложность: O(n log n), Пространственная сложность: O(log n) из-за использования стека вызовов при рекурсии.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # выбор опорного элемента (средний элемент)
        left = [x for x in arr if x < pivot]  # элементы меньше опорного
        middle = [x for x in arr if x == pivot]  # элементы равные опорному
        right = [x for x in arr if x > pivot]  # элементы больше опорного
        return quick_sort(left) + middle + quick_sort(right)

# Пример использования:
arr = [3, 6, 8, 10, 1, 2, 1]
print("Отсортированный массив:", quick_sort(arr))


## Сортировка слиянием - Временная сложность: O(n log n), O(n) для хранения временных массивов

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива на две части
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Слияние отсортированных частей
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Слияние двух массивов
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавление оставшихся элементов
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Пример использования:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)



