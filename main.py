import sys
from PyQt6.QtWidgets import QApplication
from game_window import GameWindow


def main():
    app = QApplication(sys.argv)

    # Установка стиля
    app.setStyle('Fusion')

    window = GameWindow()
    window.setWindowTitle("Agent 007 - Minefield")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()