import maxmin

# тесты
assert maxmin.get_min([9, 2, 59]) == 2, "Должно быть 2"

assert maxmin.get_max([1, 4, 27, 3]) == 27, "Должно быть 27"

assert maxmin.get_sum([1, 7, 3]) == 11, "Должно быть 11"

assert maxmin.get_mult([1, 2, 2, -1]) == -4, "Должно быть -4"

assert maxmin.get_evens_count([7, 6, 3, 6, 2]) == 3, "Должно быть 3"

# назначаем ограничение выполнения программы размеров в 1 минуту
assert maxmin.get_time(maxmin.start_time) < 60, "Время выполнения программы вышло за границы допустимого"