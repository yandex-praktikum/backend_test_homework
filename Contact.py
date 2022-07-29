class Contact:
    name: str
    year_birth: int
    is_programmer: bool

    def __init__(self,
                 name: str,
                 year_birth: int,
                 is_programmer: bool):
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def get_name(self):
        return self.name

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self) -> str:
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self) -> str:
        return(f'{self.name: str}, '
               f'категория: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())
