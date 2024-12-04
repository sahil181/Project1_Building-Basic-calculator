import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle('Python Calculator')
        self.setGeometry(100, 100, 300, 400)

        # Create display
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        grid = QGridLayout()

        # Button labels and positions
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('+', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('/', 3, 3)
        ]

        # Add buttons to the grid layout
        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, row, col)

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + text)

# Run the application
app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())
