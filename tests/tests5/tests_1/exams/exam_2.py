class Contact:
    def __init__(self, name, year_birth, is_programmer):
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return (f'{self.name}, '
                f'возраст: {self.age_define()}, '
                f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())


test_old_none_programmer = Contact('Пушкин', 1799, False)
assert test_old_none_programmer.age_define() == 'Старейшина', ('Error')

test_old_none_programmer = Contact('Пушкин', 1990, False)
assert test_old_none_programmer.age_define() == 'Молодой', ('Error')

test_old_none_programmer = Contact('Пушкин', 1950, False)
assert test_old_none_programmer.age_define() == 'Олдскул', ('Error')

test_old_none_programmer = Contact('Пушкин', 1950, False)
assert test_old_none_programmer.programmer_define() == 'Нормальный', ('Error')

test_old_none_programmer = Contact('Пушкин', 1950, True)
assert test_old_none_programmer.programmer_define() == 'Программист', ('Error')
