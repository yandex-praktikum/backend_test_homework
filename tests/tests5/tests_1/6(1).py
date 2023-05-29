import unittest


def setUpModule():
    """Вызывается один раз перед всеми классами, которые есть в файле."""
    print('> setUpModule')


def tearDownModule():
    """Вызывается один раз после всех классов, которые есть в файле."""
    print('> tearDownModule')


class TestExample(unittest.TestCase):
    """Демонстрирует принцип работы тестов."""

    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        print('>> setUpClass')

    @classmethod
    def tearDownClass(cls):
        """Вызывается один раз после запуска всех тестов класса."""
        print('>> tearDownClass')

    def setUp(self):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        print('>>> setUp')

    def tearDown(self):
        """Вызывается после каждого теста."""
        print('>>> tearDown')

    def test_one(self):  # это -- test case
        print('>>>> test_simple')

    def test_one_more(self):  # это -- ещё один test case
        print('>>>> test_simple')


if __name__ == '__main__':
    unittest.main()
