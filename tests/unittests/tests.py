import unittest
from code import series_sum  # Импорт тестируемой функции


class TestSeriesSum(unittest.TestCase):
    """Тестируем series_sum."""

    def test_mixed_numbers(self):  # Это - test case
        # Вызов тестируемой функции
        call = series_sum([1, 2.5, 3, 4])
        # Ожидаемый результат
        result = '12.534'
        # Проверка: идентичен ли результат вызова ожидаемому результату
        self.assertEqual(
            call, result, 'Функция series_sum() не работает со списком чисел'
        )

    def test_mixed_numbers_strings(self):  # И это - test case
        call = series_sum([1, 'fff', 3, 4])
        result = '1fff34'
        self.assertEqual(
            call, result, 'Функция series_sum не работает со смешанным списком'
        )

    def test_empty(self):  # И это - тоже test case
        call = series_sum([])
        result = ''
        self.assertEqual(
            call, result, 'Функция series_sum не работает с пустым списком'
        )
