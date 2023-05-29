import unittest
from typing import List


def bubble_sort(array: List[float]) -> List[float]:
    """Сортировка списка методом пузырька по возрастанию."""
    length = len(array)
    for bypass in range(1, length):
        for k in range(0, length - bypass):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array


class TestBubbleSort(unittest.TestCase):
    """Тестируем bubble_sort."""

    def test_int_float(self):
        # С несортированым списком чисел
        call = bubble_sort([10, 3, 5.0, 1])
        result = [1, 3, 5.0, 10]
        self.assertEqual(
            call, result,
            'Функция bubble_sort не работает со списком чисел'
        )

    def test_empty(self):
        # С пустым списком
        call = bubble_sort([])
        result = []
        self.assertEqual(
            call, result,
            'Функция bubble_sort не работает с пустым списком'
        )
