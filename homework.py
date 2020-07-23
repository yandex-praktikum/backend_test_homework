import datetime as dt


class Calculator:
    """
    Родительский класс калькулятора, для подсчёта
    денег и калорий.
    """
    def __init__(self, limit):
        """
        Инициализатор класса Calculator, имеет в себе 
        аргумент limit, который задаёт лимит калькулятору.
        """
        self.limit = limit
        self.records = []

    def add_record(self, some_record):
        """
        Метод add_record добавляет в список данные
        полученные из объекта класса Record.
        """
        self.records.append(some_record)

    def get_today_stats(self):
        """
        Метод get_today_stats считает сумму потраченного
        (amount) за сегодняшний день.
        """
        amount_today = 0
        date_today = dt.date.today()
        for record in self.records:
            if record.date == date_today:
                amount_today += record.amount
        return amount_today 

    def get_week_stats(self):
        """
        Метод get_week_stats считает сумму 
        потраченного(amount) за послелние 7 дней.
        """
        amount_week = 0
        date_today = dt.datetime.today().date()
        for record in self.records:
            if record.date <= date_today and record.date >= (date_today - dt.timedelta(days=7)):
                amount_week += record.amount
        return amount_week 
    
    def cash_remained(self):
        return (round(self.limit - self.get_today_stats(), 2)) 

            
class Record:
    def __init__(self, amount, comment, date = None):
        """
        Класс Record имеет 3 аргумента: amount - потраченные деньги
        или полученные калории, комментарий и дата(если даты нет, то она 
        присваивается по умолчания сегодняшним днём)
        """
        self.amount = amount
        self.comment = comment 
        if date == None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
            
class CashCalculator(Calculator):
    """
    Наследованный класс CashCalculator.
    Имеет метод get_today_cash_remained.
    """
    USD_RATE = 70.0
    EURO_RATE = 80.0    
    def get_today_cash_remained(self, currency):
        """
        Метод get_today_cash_remained считает сколько
        еще можно потратить если лимит не превышен.
        Если лимит превышен то сообщает сумму долга.
        """
        #cash_remained = self.limit - self.get_today_stats()
        if self.get_today_stats() < self.limit:   
            if self.currency == 'rub':
                return f'На сегодня осталось {round(cash_remained, 2)} руб'
            elif self.currency == 'usd':
                return f'На сегодня осталось {round((cash_remained / CashCalculator.USD_RATE), 2)} USD'
            else:
                return f'На сегодня осталось {round((cash_remained / CashCalculator.EURO_RATE), 2)} Euro'
        elif super().get_today_stats() == self.limit:
            return 'Денег нет, держись'
        else:
            if self.currency == 'rub':
                return f'Денег нет, держись: твой долг - {-(round(cash_remained, 2))} руб'
            elif self.currency == 'usd':
                return f'Денег нет, держись: твой долг - {-(round((cash_remained / CashCalculator.USD_RATE), 2))} USD'
            else:
                return f'Денег нет, держись: твой долг - {-(round((cash_remained / CashCalculator.EURO_RATE), 2))} Euro'

class CaloriesCalculator(Calculator):
    """
    Наследованный класс CaloriesCalculator.

    Имеет метод get_calories_remained.
    """
    def get_calories_remained(self):
        """
        Метод get_calories_remained считает сколько

        еще можно съесть калорий если лимит не превышен.
        Если лимит превышен, сообщает об этом.
        """
        calories_remained = self.limit - self.get_today_stats()
        if self.get_today_stats() < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {round((calories_remained), 2)} кКал'
        else:
            return 'Хватит есть!'

cash_calculator = CashCalculator(1000) # Дневной лимит калькулятора денег
calories_calculator = CaloriesCalculator(1000) # Дневной лимит калькулятора калорий


cash_calculator.add_record(Record(amount = 330, comment = 'Пирожки', date = '10.07.2020')) # создание объектов класса Record
cash_calculator.add_record(Record(amount = 100, comment = 'Яблоки', date = '11.07.2020'))
cash_calculator.add_record(Record(amount = 670.23, comment = 'Кофе 1 кг', date = '12.07.2020'))
cash_calculator.add_record(Record(amount = 250, comment = 'Парикмахер', date = '13.07.2020'))
cash_calculator.add_record(Record(amount = 80, comment = 'Мороженое', date = '14.07.2020'))
cash_calculator.add_record(Record(amount = 100, comment = 'Шоколадка', date = '18.07.2020'))
cash_calculator.add_record(Record(amount = 1120, comment = 'Помидоры'))

calories_calculator.add_record(Record(amount = 130, comment = 'Печенье', date = '10.07.2020'))
calories_calculator.add_record(Record(amount = 100, comment = 'Конфеты', date = '11.07.2020'))
calories_calculator.add_record(Record(amount = 170.23, comment = 'Шоколад', date = '12.07.2020'))
calories_calculator.add_record(Record(amount = 250, comment = 'Стейк', date = '13.07.2020'))
calories_calculator.add_record(Record(amount = 80, comment = 'Салат', date = '14.07.2020'))
calories_calculator.add_record(Record(amount = 100, comment = 'Йогурт', date = '18.07.2020'))
calories_calculator.add_record(Record(amount = 120, comment = 'Клубника'))


print(cash_calculator.get_today_stats())                  # вызовы методов 
print(cash_calculator.get_week_stats())
print(cash_calculator.get_today_cash_remained('rub'))
print(calories_calculator.get_today_stats())
print(calories_calculator.get_week_stats())
print(calories_calculator.get_calories_remained())
