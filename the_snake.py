"""
Игра 'Змейка'.

Содержит классы GameObject, Snake, Apple и основной игровой цикл.
"""

from random import choice, randint
import pygame


# --- Константы ---
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

SPEED = 20

pygame.init()
pygame.display.set_caption('Змейка')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()


class GameObject:
    """
    Базовый класс игрового объекта.

    Атрибуты:
        position (tuple): координаты объекта.
        body_color (tuple): цвет объекта (RGB).
    """

    def __init__(self, position=None, body_color=None):
        """Инициализирует объект базовой позицией и цветом."""
        center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.position = position if position is not None else center
        self.body_color = body_color

    def draw(self):
        """Переопределяется в дочерних классах."""
        pass


class Apple(GameObject):
    """
    Класс яблока.

    Яблоко появляется в случайной позиции
    и увеличивает длину змейки при съедании.
    """

    def __init__(self, body_color=APPLE_COLOR):
        """Создаёт яблоко со случайной позицией и заданным цветом."""
        pos = self.randomize_position()
        super().__init__(pos, body_color)

    def randomize_position(self):
        """Возвращает новую случайную позицию яблока в пределах сетки."""
        x = randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        self.position = (x, y)
        return self.position

    def draw(self):
        """Отрисовывает яблоко на экране."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """
    Класс змейки.

    Атрибуты:
        length (int): длина змейки.
        positions (list): координаты сегментов тела.
        direction (tuple): текущее направление движения.
        next_direction (tuple): направление, выбранное игроком.
        last (tuple|None): координаты удалённого хвостового сегмента.
    """

    def __init__(self, body_color=SNAKE_COLOR):
        """Создаёт змейку в центре с длиной 1 и направлением вправо."""
        center_x = (GRID_WIDTH // 2) * GRID_SIZE
        center_y = (GRID_HEIGHT // 2) * GRID_SIZE
        start = (center_x, center_y)

        self.length = 1
        self.positions = [start]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

        super().__init__(start, body_color)

    def update_direction(self):
        """Обновляет направление движения."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """
        Перемещает змейку.

        Добавляет новую голову по направлению движения и удаляет хвост,
        если длина не увеличилась. Проверяет столкновение с собой.
        """
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction
        new_head = (
            (head_x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT,
        )

        if new_head in self.positions[2:]:
            self.reset()
            return

        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.last = self.positions[-1]
            self.positions.pop()
        else:
            self.last = None

        self.position = new_head

    def draw(self):
        """Отрисовывает голову и тело змейки."""
        for pos in self.positions[1:]:
            rect = pygame.Rect(pos, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        center_x = (GRID_WIDTH // 2) * GRID_SIZE
        center_y = (GRID_HEIGHT // 2) * GRID_SIZE
        start = (center_x, center_y)

        self.length = 1
        self.positions = [start]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None
        self.last = None
        self.position = start

        screen.fill(BOARD_BACKGROUND_COLOR)


def handle_keys(game_object):
    """Обрабатывает нажатия клавиш игрока."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main(run_once=False):
    """
    Основной игровой цикл.

    Если run_once=True — игра делает один тик (нужно для тестов).
    """
    snake = Snake(body_color=SNAKE_COLOR)
    apple = Apple(body_color=APPLE_COLOR)

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw()
        snake.draw()
        pygame.display.update()

        if run_once:
            break


if __name__ == '__main__':
    main()
