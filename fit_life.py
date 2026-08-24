# Проект FitLife - MVP версия 1.0

class Training:
    """Базовый класс для тренировки"""
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        """Считает ИМТ и возвращает округлённое значение"""
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 1)

# 1. Сбор данных
#user_name = input('Как тебя зовут? ')
#user_age = int(input('Сколько тебе лет? '))
#user_weight = float(input('Какой у тебя вес в кг? '))
#user_height = float(input('Какой у тебя рост в метрах 
#(например, 1.75)? '))
user_name = 'Antonina'
user_age = 50
user_weight = 70.0
user_height = 1.70

# 2. Расчеты
my_training = Training(user_weight, user_height)
bmi = my_training.calculate_bmi()
water_needed = user_weight * 30 

# 3. Вывод результата
print(f'Возраст: {user_age} лет')
print(f'ИМТ: {bmi}')
print(f'Норма воды: {water_needed} мл') 
print('Расчет окончен. Будьте здоровы!')
