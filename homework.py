class InfoMessage():
    """Класс для создания объектов сообщений."""
    def __init__(self, training_type: str, duration: float, distance: float,
                 speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def show_training_info(self):
        # вызвать функцию округления для дистанции
        message = (f'Тип тренировки: {self.training_type};'
                   f'Длительность: {self.duration:.3f} ч.;'
                   f'Дистанция: {self.distance:.3f} км;'
                   f'Ср. скорость: {self.speed:.3f} км/ч;'
                   f'Потрачено ккал: {self.calories:.3f}.'
                   )
        return message


class Training:

    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Возвращает дистанцию (в километрах), которую преодолел пользователь
        за время тренировки."""
        return self.action * Training.LEN_STEP / Training.M_IN_KM

    def get_mean_speed(self) -> float:
        """Возвращает значение средней скорости движения во время тренировки.
        Формула = преодоленная_дистанция_за_тренировку / время_тренировки.
        """
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных
        за время тренировки.
        """
        pass

    def show_training_info(self, training_type, calories) -> InfoMessage:
        """Возвращает объект класса сообщения о результатах тренировки."""
        info = InfoMessage(training_type, self.duration, self.get_distance(),
                           self.get_mean_speed(), calories)
        return info


class Running(Training):
    """Бег"""

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Расход калорий для бега.
        (18 * средняя_скорость - 20) * вес_спортсмена /
        M_IN_KM * время_тренировки_в_минутах)
        """
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        calories_Running = ((
            coeff_calorie_1
            * self.get_mean_speed()
            - coeff_calorie_2)
            * self.weight
            / Training.M_IN_KM
            * (self.duration * 60))
        return calories_Running


class SportsWalking(Training):
    """Спортивная ходьба"""

    def __init__(self, action: int, duration: float, weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Расчет (0.035 * вес + (средняя_скорость**2 // рост) *
        0.029 * вес) * время_тренировки_в_минутах)
        """

        coeff_calorie_3 = 0.035
        coeff_calorie_4 = 0.029

        calories_SportsWalking = ((
            coeff_calorie_3
            * self.weight
            + (self.get_mean_speed()**2
            // self.height)
            * coeff_calorie_4
            * self.weight)
            * (self.duration * 60))
        return calories_SportsWalking


class Swimming(Training):
    """Плавание"""

    LEN_STEP = 1.38

    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Формула расчёта средней скорости при плавании:
        длина_бассейна * count_pool / M_IN_KM / время_тренировки.
         """
        mean_speed_Swimming = (self.length_pool
                               * self.count_pool
                               / Training.M_IN_KM
                               / (self.duration * 60)
                               )
        return mean_speed_Swimming

    def get_spent_calories(self) -> float:
        """Формула для расчёта израсходованных калорий
        (средняя_скорость + 1.1) * 2 * вес
        """
        coeff_calorie_5 = 1.1

        calories_Swimming = (self.get_mean_speed() +
                             coeff_calorie_5) * 2 * self.weight
        return calories_Swimming


def read_package(workout_type: str, data: list[float]) -> Training:
    """Прочитать данные, полученные от датчиков."""

    workout_type_and_class = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    traning = workout_type_and_class[workout_type](*data)
    return traning


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info(training.__doc__,
                                       training.get_spent_calories())
    print(info.show_training_info())


if __name__ == "__main__":
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]
    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
