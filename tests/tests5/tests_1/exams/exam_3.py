def test_sort(sorting_algorithm):
    """ Тестируем алгоритм, сортирующий список по возрастанию."""
    print(f'Тестируем: {sorting_algorithm.__doc__}')

    # Ваш код здесь
    assert sorting_algorithm([2, 6.6, 4]) == [2, 4, 6.6], ('Error')
    assert sorting_algorithm([2, 6, -4]) == [-4, 2, 6], ('Error')
    assert sorting_algorithm([2, 4, 4]) == [2, 4, 4], ('Error')
    assert sorting_algorithm([]) == [], ('Error')
    print(f'Тест для {sorting_algorithm.__name__} завершён')


sort_funcs = [
    bubble_sort,
    timsort_sort,
    selection_sort,
    insertion_sort,
    cap_sort,
    merge_sort,
    heap_sort,
    stepa_sort,
    quick_sort,
    sus_sort,
]
for func in sort_funcs:
    try:
        test_sort(func)
    except AssertionError as e:
        print(str(e))
