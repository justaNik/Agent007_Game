from PyQt6.QtWidgets import (QMainWindow, QMessageBox, QPushButton,
                             QLabel, QVBoxLayout, QWidget, QSizePolicy)
from functools import partial
from agentint import Ui_MainWindow
from game_logic import GameLogic


class GameWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sizeSpinBox.setValue(18)
        self.game = GameLogic(size=self.sizeSpinBox.value())
        self.init_ui()
        self.update_ui()
        self.restartButton.clicked.connect(self.reset_game)

    def init_ui(self):
        self.cells = []
        for y in range(self.game.size):
            row = []
            for x in range(self.game.size):
                btn = QPushButton(parent=self.gridLayoutWidget)
                #btn.setFixedSize(30, 30)
                btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                btn.setMinimumSize(10, 10)

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

        self.resize_cells()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_cells()

    def resize_cells(self):
        if not self.cells:
            return

        layout_width = self.gridLayoutWidget.width()
        layout_height = self.gridLayoutWidget.height()

        cell_width = layout_width // self.game.size
        cell_height = layout_height // self.game.size
        cell_size = min(cell_width, cell_height)

        for row in self.cells:
            for btn in row:
                btn.setFixedSize(cell_size, cell_size)

    def reset_game(self):
        size = self.sizeSpinBox.value()
        self.game = GameLogic(size=size)

        # удаляем старые кнопки
        for row in self.cells:
            for btn in row:
                btn.setParent(None)

        # создем новые кнопки
        self.init_ui()
        self.update_ui()
        self.resize_cells()

    def update_ui(self):
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

                if (x, y) == self.game.current_pos:
                    btn.setStyleSheet("background-color: gold;")
                elif (x, y) in self.game.path:
                    btn.setStyleSheet("background-color: #ADD8E6;")
                elif (x, y) in self.game.mines:
                    btn.setStyleSheet("background-color: black; color: white;")
                elif (x, y) in self.game.visited:
                    btn.setStyleSheet("background-color: #E0E0E0;")
                elif not self.game.game_over:
                    btn.setStyleSheet("background-color: #90EE90;")
                else:
                    btn.setStyleSheet("background-color: white;")

        if self.game.game_over:
            if self.game.exploded_mine:
                x, y = self.game.exploded_mine
                self.cells[y][x].setStyleSheet("background-color: red; color: white;")
                self.cells[y][x].setText("💥")
                QMessageBox.information(self, "Game Over", "You hit a mine! Game over.")
            elif self.game.win:
                QMessageBox.information(self, "Congratulations!", "You won! All safe cells visited.")

    def on_cell_click(self, x, y):
        if self.game.game_over:
            return
        success = self.game.make_move((x, y))
        self.update_ui()
