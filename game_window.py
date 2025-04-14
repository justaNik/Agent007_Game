from PyQt6.QtWidgets import (QMainWindow, QMessageBox, QPushButton,
                             QLabel, QVBoxLayout, QWidget)
from functools import partial
from agentint import Ui_MainWindow
from game_logic import GameLogic


class GameWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.game = GameLogic()
        self.init_ui()
        self.update_ui()
        self.possible_moves = []
        self.restartButton.clicked.connect(self.reset_game)

    def init_ui(self):
        self.cells = []
        for y in range(self.game.size):
            row = []
            for x in range(self.game.size):
                btn = QPushButton(parent=self.gridLayoutWidget)
                btn.setFixedSize(30, 30)
                # Используем partial для передачи координат
                btn.clicked.connect(partial(self.on_cell_click, x, y))
                self.gridLayout_2.addWidget(btn, y, x)
                row.append(btn)
            self.cells.append(row)

        self.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                border: 1px solid #555;
            }
            QLabel {
                font-size: 14px;
            }
        """)

    def update_ui(self):
        #self.boxesLabel.setText(f"Visited: {visited_count}/{total_safe}")
        #self.scoreLabel.setText(f"Current position: {self.game.current_pos}")
        self.scoreLabel.setText(f"Score: {self.game.score}")

        for y in range(self.game.size):
            for x in range(self.game.size):
                btn = self.cells[y][x]
                value = self.game.get_cell_value(x, y)

                if (x, y) == self.game.current_pos:
                    btn.setText("★")
                elif (x, y) in self.game.mines:
                    btn.setText("💣")
                else:
                    btn.setText(str(value))

                # Стиль кнопок
                if (x, y) == self.game.current_pos:
                    btn.setStyleSheet("background-color: gold;")
                elif (x, y) in self.game.path:
                    btn.setStyleSheet("background-color: #ADD8E6;")  # Путь — голубой
                elif (x, y) in self.game.mines:
                    btn.setStyleSheet("background-color: black; color: white;")
                elif (x, y) in self.game.visited:
                    btn.setStyleSheet("background-color: #E0E0E0;")
                elif not self.game.game_over:
                    btn.setStyleSheet("background-color: #90EE90;")
                else:
                    btn.setStyleSheet("background-color: white;")

        if self.game.game_over:
            if hasattr(self.game, 'exploded_mine'):
                x, y = self.game.exploded_mine
                self.cells[y][x].setStyleSheet("background-color: red; color: white;")
                self.cells[y][x].setText("💥")
                QMessageBox.information(self, "Game Over", "You hit a mine! Game over.")
            elif self.game.win:
                QMessageBox.information(self, "Congratulations!", "You won! All safe cells visited.")

    def on_cell_click(self, x, y):
        print("Клик!")
        print(f"Нажата клетка: ({x}, {y})")

        if self.game.game_over:
            return

        success = self.game.make_move((x, y))
        if success:
            print("Ход выполнен")
        else:
            print("Игра окончена или недопустимый ход (вышел за границы или мина)")
        self.update_ui()

    def reset_game(self):
        self.game.score = 0
        self.game.reset_game()
        self.update_ui()

