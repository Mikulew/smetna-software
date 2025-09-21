import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Przycisk demo")
        self.setGeometry(300, 300, 300, 200)
        self.howmanyclicks = 0
        # Layout pionowy
        layout = QVBoxLayout()

        # Etykieta
        self.label = QLabel("Kliknij przycisk")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # Przycisk
        self.button = QPushButton("Kliknij mnie")
        layout.addWidget(self.button)

        # Powiązanie przycisku z funkcją
        self.button.clicked.connect(self.on_button_click)

        self.setLayout(layout)

    

    def on_button_click(self):
        self.label.setText("Przycisk został kliknięty 🎉")
        self.howmanyclicks += 1
        if (self.howmanyclicks >= 10): 
            self.label.setText("Dobra słyszałem za pierwszym razem ☠️")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())