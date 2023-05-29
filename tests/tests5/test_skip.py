import sys
import unittest


class TestExample(unittest.TestCase):
    """Демонстрирует возможности по пропуску тестов."""

    @unittest.skip('Этот тест мы просто пропускаем')
    def test_show_msg(self):
        self.assertTrue(False, 'Значение должно быть истинным')

    @unittest.skipIf(
        sys.version_info.major == 3 and sys.version_info.minor == 9,
        'Пропускаем, если питон 3.9'
        )
    def test_python3_9(self):
        # Тест будет запущен, только если версия питона отлична от 3.9.
        # В условиях можно проверять версии библиотек, доступность внешних сервисов,
        # время или дату - любые данные
        pass

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Тест только для Linux'
        )
    def test_linux_support(self):
        # Тест будет запущен только в Linux
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(False, 'Ожидаем истинное значение')


if __name__ == '__main__':
    unittest.main()
