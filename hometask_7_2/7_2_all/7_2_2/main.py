from PyQt6.QtWidgets import *
app = QApplication([])
window = QWidget()
label = QLabel('TopQLabel as label in one window')
layout = QFormLayout()
layout.addWidget(label)
layout.addRow(('Top Button Label:'), QPushButton('Top'))
layout.addRow(('Bottom Button Label:'), QPushButton('Bottom'))
window.setLayout(layout)
window.setWindowTitle('Advanced title for QFormLayout')
window.show()
app.exec()