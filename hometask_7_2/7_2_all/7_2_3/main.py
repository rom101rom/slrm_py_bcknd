from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
class ClickerWindow(QWidget):
    '''Window with 3 buttons: message-box, checked label and clicker-counter'''

    def __init__(self):
        super().__init__()
        
    
        self.layout = QVBoxLayout()

        self.button_is_checked = True
        self.clicked_count = 0
        self.label = QLabel('Checked', self)

        self.clickButton = QPushButton('Click', self)
        self.checkedButton = QPushButton()
        self.checkedButton.setCheckable(True)
        self.checkedButton.setChecked(self.button_is_checked)
        self.counterButton = QPushButton('Click count = 0', self)
        
        self.layout.addWidget(self.clickButton)
        self.layout.addWidget(self.checkedButton)
        self.layout.addWidget(self.counterButton)
        self.layout.addWidget(self.label)
        
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        self.clickButton.clicked.connect(self.on_clickButton_clicked)
        self.checkedButton.clicked.connect(self.on_checkedButton_clicked)
        self.counterButton.clicked.connect(self.on_counterButton_clicked)

        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Clicker counter')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_clickButton_clicked(self):
        alert = QMessageBox()
        alert.setText('You clicked the button!')
        alert.exec()

    def on_checkedButton_clicked(self, checked):

        self.checkedButton.setText('ON' if checked else 'OFF')
        self.label.setVisible(checked)


    def on_counterButton_clicked(self):
        global clicked_count
        self.clicked_count += 1
        self.counterButton.setText(f'Click count = {self.clicked_count}')


if __name__ == '__main__':

    app = QApplication([])
    my_window = ClickerWindow()

    app.exec()