import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 400, 300)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add widgets (e.g., buttons) to the layout
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Set the layout for this window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
