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
        self.hit_wall = False

        self.place_mines()
        self.set_start_position()

    def place_mines(self):
        total_mines = random.randint(self.min_mines, self.max_mines)
        while len(self.mines) < total_mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.mines.add((x, y))
            self.board[y][x] = -1  # Обозначаем мину

    def set_start_position(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) not in self.mines:
                self.current_pos = (x, y)
                self.visited.add((x, y))
                break

    def make_move(self, new_pos: Tuple[int, int]) -> bool:
        if self.game_over:
            return False

        if not self.current_pos:
            return False

        start_x, start_y = self.current_pos
        x, y = new_pos

        # Ход возможен только на соседнюю клетку
        if abs(x - start_x) > 1 or abs(y - start_y) > 1 or (x == start_x and y == start_y):
            return False

        # Определяем направление
        dx = x - start_x
        dy = y - start_y

        dx = 0 if dx == 0 else (1 if dx > 0 else -1)
        dy = 0 if dy == 0 else (1 if dy > 0 else -1)

        steps = self.board[y][x]
        self.path = []

        for step in range(1, steps + 1):
            nx = start_x + dx * step
            ny = start_y + dy * step

            if not (0 <= nx < self.size and 0 <= ny < self.size):
                self.hit_wall = True
                self.game_over = True
                return False

            if (nx, ny) in self.mines:
                self.game_over = True
                self.exploded_mine = (nx, ny)
                return False

            self.path.append((nx, ny))
            self.score += self.board[nx][ny]

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
        return (x, y) in self.visited

    def is_mine(self, x: int, y: int) -> bool:
        return (x, y) in self.mines
