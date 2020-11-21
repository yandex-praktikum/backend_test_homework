import datetime as dt


class Record:
    date_format = '%d.%m.%Y'
    records = []

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, self.date_format).date()
        else:
            self.date = dt.date.today()

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        return self.records

    def get_today_stats(self):
        self.today = dt.date.today()
        return sum(record.amount for record in self.records if record.date == self.today)

    def get_week_stats(self):
        self.sum_week = 0
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)
        return sum(record.amount for record in self.records
                   if self.today >= record.date >= self.week_ago)

class CashCalculator(Calculator):
    RUB_RATE = 1
    USD_RATE = 60.00
    EURO_RATE = 70.00

    def __init__(self,limit ):
        super().__init__(limit)
        self.currencies = {'rub':'руб','usd':'USD','eur':'Euro'}


    def get_today_cash_remained(self,currency):
        remained = self.limit - self.get_today_stats()

        if currency == 'rub':
            remained = remained / self.RUB_RATE
        elif currency == 'usd':
            remained = remained / self.USD_RATE
        elif currency == 'eur':
            remained = remained / self.EURO_RATE

        if remained > 0:
            return(f'На сегодня осталось {remained:.2f} {self.currencies[currency]}')
        elif remained == 0:
            return('Денег нет, держись')
        else:
            return(f'Денег нет, держись: твой долг - {abs(remained):.2f} {self.currencies[currency]}')

    def add_record(self,record):
        self.records.append(record)

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        self.remained = self.limit - self.get_today_stats()

    def get_calories_remained(self):
        self.remained = self.limit - self.get_today_stats()
        if self.remained > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью'
                    f' не более {self.remained} кКал')
        else:
            return ('Хватит есть!')

    def add_record(self,record):
        self.records.append(record)






