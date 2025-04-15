import random
from typing import Tuple, List, Set, Optional


class GameLogic:
    def __init__(self, size=18, min_mines=10, max_mines=15, min_way=1, max_way=6):
        self.size = size
        self.min_mines = min_mines
        self.max_mines = max_mines
        self.min_way = min_way
        self.max_way = max_way
        self.exploded_mine = None
        self.reset_game()

    def reset_game(self):
        """Инициализация новой игры"""
        # перенести цифры 1 и 6 в параметры конструктора
        self.board = [[random.randint(self.min_way, self.max_way) for _ in range(self.size)] for _ in range(self.size)]
        self.mines = set()
        self.visited = set()  # Посещенные клетки
        self.current_pos = None  # Текущая позиция агента
        self.game_over = False
        self.win = False
        self.path = []  # Текущий путь хода
        self.score = 0

        self.place_mines()
        self.set_start_position()

    def place_mines(self):
        """Расстановка видимых мин на поле"""
        total_mines = random.randint(self.min_mines, self.max_mines)
        while len(self.mines) < total_mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.mines.add((x, y))
            self.board[y][x] = -1  # Обозначаем мину

    def set_start_position(self):
        """Выбор случайной стартовой позиции"""
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) not in self.mines:
                self.current_pos = (x, y)
                self.visited.add((x, y))
                break

    '''def get_possible_moves(self) -> List[Tuple[int, int]]:
        """Возвращает список соседних клеток, из которых можно сделать ход"""
        if not self.current_pos or self.game_over:
            return []

        x, y = self.current_pos
        moves = []

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < self.size and 0 <= ny < self.size):
                continue

            if (nx, ny) in self.visited:
                continue

            steps = self.board[ny][nx]

            # Проверка — не выйдет ли за границы
            end_x = x + dx * steps
            end_y = y + dy * steps

            if not (0 <= end_x < self.size and 0 <= end_y < self.size):
                continue

            moves.append((nx, ny))

        return moves'''

    def make_move(self, new_pos: Tuple[int, int]) -> bool:
        """Выполнение хода: направление определяется по выбранной соседней клетке,
        затем идем на число шагов в этом направлении"""
        '''if self.game_over or new_pos not in self.get_possible_moves():
            return False'''
        if self.game_over:
            return False

        start_x, start_y = self.current_pos
        dir_x = new_pos[0] - start_x
        dir_y = new_pos[1] - start_y

        # Направление должно быть -1, 0 или 1
        dx = 0 if dir_x == 0 else (1 if dir_x > 0 else -1)
        dy = 0 if dir_y == 0 else (1 if dir_y > 0 else -1)

        # Число шагов берем из выбранной клетки
        steps = self.board[new_pos[1]][new_pos[0]]
        self.path = []

        for step in range(1, steps + 1):
            x = start_x + dx * step
            y = start_y + dy * step

            # Проверка выхода за границы
            if not (0 <= x < self.size and 0 <= y < self.size):
                self.game_over = True
                return False

            # Проверка на мину
            if (x, y) in self.mines:
                self.game_over = True
                self.exploded_mine = (x, y)
                return False

            self.path.append((x, y))
            self.score += self.board[x][y]

        # Обновляем состояние
        for cell in self.path:
            self.visited.add(cell)
        self.current_pos = self.path[-1]

        if len(self.visited) == self.size * self.size - len(self.mines):
            self.win = True
            self.game_over = True

        return True

    def get_cell_value(self, x: int, y: int) -> int:
        """Возвращает значение клетки (-1 для мин)"""
        return self.board[y][x]

    def is_visited(self, x: int, y: int) -> bool:
        """Проверяет, посещена ли клетка"""
        return (x, y) in self.visited

    def is_mine(self, x: int, y: int) -> bool:
        """Проверяет, является ли клетка миной"""
        return (x, y) in self.mines
