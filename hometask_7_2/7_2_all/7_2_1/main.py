from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase

app = QApplication([])
my_font = QFont("Magneto", 44)
label = QLabel('Hello World!')
label.setFixedSize(500, 100)
label.setFont(my_font)
label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
label.show()
app.exec()