from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import sys
from gui.assets import get_avatar_path

def start_gui():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Kiko AI")
    window.setGeometry(100, 100, 300, 300)

    layout = QVBoxLayout()

    avatar_label = QLabel()
    avatar_path = get_avatar_path()
    movie = QMovie(avatar_path)
    avatar_label.setMovie(movie)
    movie.start()

    layout.addWidget(avatar_label, alignment=Qt.AlignCenter)
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())
