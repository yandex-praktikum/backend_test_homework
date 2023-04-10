from dataclasses import dataclass, InitVar


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (
            f'Тип тренировки: {self.training_type}; '
            f'Длительность: {self.duration:.3f} ч.; '
            f'Дистанция: {self.distance:.3f} км; '
            f'Ср. скорость: {self.speed:.3f} км/ч; '
            f'Потрачено ккал: {self.calories:.3f}.'
        )


@dataclass
class Training:
    """Базовый класс тренировки."""
    action: int
    duration: float
    weight: float

    LEN_STEP = 0.65
    M_IN_KM = 1000
    MIN_IN_H = 60

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__, self.duration,
            self.get_distance(), self.get_mean_speed(),
            self.get_spent_calories()
        )


@dataclass
class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER: InitVar[int] = 18
    CALORIES_MEAN_SPEED_SHIFT: InitVar[float] = 1.79

    def get_spent_calories(self) -> float:
        return (
            (self.CALORIES_MEAN_SPEED_MULTIPLIER
             * self.get_mean_speed()
             + self.CALORIES_MEAN_SPEED_SHIFT)
            * self.weight / self.M_IN_KM
            * (self.duration * self.MIN_IN_H)
        )


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    height: float
    PAR_FOR_FORMUL_1: InitVar[float] = 0.035
    PAR_FOR_FORMUL_2: InitVar[float] = 0.029
    KM_IN_M: InitVar[float] = 0.278
    H_IN_SM: InitVar[int] = 100

    def get_spent_calories(self) -> float:
        return (
            (self.PAR_FOR_FORMUL_1 * self.weight
             + ((self.get_mean_speed() * self.KM_IN_M) ** 2
                 / (self.height / self.H_IN_SM))
             * self.PAR_FOR_FORMUL_2 * self.weight)
            * (self.duration * self.MIN_IN_H)
        )


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    length_pool: float
    count_pool: int
    LEN_STEP: InitVar[float] = 1.38
    PAR_FOR_FORMULA_1: InitVar[float] = 1.1
    PAR_FOR_FORMULA_2: InitVar[float] = 2

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return (
            (self.get_mean_speed() + self.PAR_FOR_FORMULA_1)
            * self.PAR_FOR_FORMULA_2
            * self.weight * self.duration
        )


MSG_ERROR = 'Тренировки типа {} не существует'


def read_package(workout_type: str, data: list[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    pack_dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    training_class = pack_dict.get(workout_type)
    if not training_class:
        raise ValueError(MSG_ERROR.format(workout_type))
    return training_class(*data)


def main(training: Training) -> None:
    """Главная функция."""
    info: str = training.show_training_info().get_message()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
