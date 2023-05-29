def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам.
    result = ''
    for i in incoming:
        result += str(i)
    return result

# Первое тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из целых и дробных чисел.


mixed_numbers = [1, 5.6]
result_numbers = '15.6'

# Вместо многоточия напишите утверждение, которое должно быть проверено
assert series_sum(mixed_numbers) == result_numbers, (
    'Функция series_sum() не работает со списком чисел')

# Второе тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из чисел и строк.

mixed_numbers_strings = [1, 5.6, 'qwe']
result_numbers_strings = '15.6qwe'

# Вместо многоточия напишите утверждение, которое должно быть проверено
assert series_sum(mixed_numbers_strings) == result_numbers_strings, (
    'Функция series_sum() не работает со смешанным списком')

# Третье тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать пустой список.
empty = []
result_empty = ''

# Вместо многоточия напишите утверждение, которое должно быть проверено
assert series_sum(empty) == result_empty, (
    'Функция series_sum() не работает с пустым списком')


print(series_sum([]))
