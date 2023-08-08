from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton, QComboBox

import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Average Speed Calculator')

        grid = QGridLayout()

        distance = QLabel('Distance')
        self.distance_enter = QLineEdit()

        time = QLabel('Time (hours)')
        self.time_enter = QLineEdit()

        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel('')

        self.combo = QComboBox()
        self.combo.addItems(['Metric(km)', 'Imperial(miles)'])

        grid.addWidget(distance, 0, 0)
        grid.addWidget(self.distance_enter, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time, 1, 0)
        grid.addWidget(self.time_enter, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0)

        self.setLayout(grid)

    def calculate_speed(self):
        if self.combo.currentIndex() == 0:
            dt = self.distance_enter.text()
            time = self.time_enter.text()
            speed = float(dt) / float(time)
            self.output_label.setText(f'Average Speed: {speed} km/h')
        elif self.combo.currentIndex() == 1:
            dt = self.distance_enter.text()
            time = self.time_enter.text()
            speed = float(dt) / float(time)
            self.output_label.setText(f'Average Speed: {speed} mph')


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
