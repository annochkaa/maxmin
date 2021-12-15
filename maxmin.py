import time

# функция нахождения минимума
def get_min(array):
    min = array[0]
    for i in range(len(array)):
        if (array[i] < min):
            min = array[i]
    return min

# функция нахождения максимума
def get_max(array):
    max = array[0]
    for i in range(len(array)):
        if (array[i] > max):
            max = array[i]
    return max

# функция нахождения суммы
def get_sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

# функция нахождения произведения
def get_mult(array):
    p = 1
    for i in range(len(array)):
        p *= array[i]
    return p

# функция нахождения затраченного времени
def get_time(start_time):
    return time.time() - start_time

# функция нахождения количества чётных чисел (для доп. теста)
def get_evens_count(array):
    evens = 0
    for i in range(len(array)):
        if (array[i] % 2 == 0):
            evens += 1
    return evens

# запускаем таймер для проверки скорости программы
start_time = time.time() 

# открыть файл
file = open("sequence.txt", "r")
# прочитать файл и конвертировать в массив строк,
# разделителем строки считаем 'пробел'
numbers = file.read().split(' ')

# переводим массив строк в массив чисел
numbers = list(map(int, numbers))

try:
    # печать в консоль результатов функций
    print("Минимальное: %d" % get_min(numbers))
    print("Максимальное: %d" % get_max(numbers))
    print("Сумма: %d" % get_sum(numbers))
    print("Произведение: %d" % get_mult(numbers))
except OverflowError:
    print("Ошибка переполнения")

print("Затраченное время: %f секунд" % get_time(start_time))