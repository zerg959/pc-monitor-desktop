import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QProgressBar,
    QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QLineEdit
)
from PySide6.QtCore import Qt, QSize, QTime, QTimer
from PySide6.QtGui import QFont
from history_window import HistoryWindow
from app_logic import AppLogic


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PC Monitor")
        self.setGeometry(100, 100, 600, 400)

        main_layout = QVBoxLayout()
        # Current time Label
        current_time_label = QLabel("Current time")
        current_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(current_time_label)
        # Time label
        self.time_label = QLabel("")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.time_label)

        # Recording Time label
        self.recording_time_label = QLabel("Recording time: 00:00:00")
        self.recording_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.recording_time_label)

        # Add spacer before widgets to center them vertically
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # CPU Section
        cpu_layout = QHBoxLayout()
        cpu_label = QLabel("CPU Usage:")
        cpu_label.setFont(QFont("Arial", 12))
        self.cpu_progress = QProgressBar()
        self.cpu_progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_progress.setTextVisible(True)
        self.cpu_progress.setMinimumSize(150, 20)
        self.cpu_progress.setMaximumSize(300, 20)
        self.cpu_percent_label = QLabel("0 %")
        cpu_layout.addWidget(cpu_label)
        cpu_layout.addWidget(self.cpu_progress)
        cpu_layout.addWidget(self.cpu_percent_label)
        main_layout.addLayout(cpu_layout)

        # RAM Section
        ram_layout = QHBoxLayout()
        ram_label = QLabel("RAM Usage:")
        ram_label.setFont(QFont("Arial", 12))
        self.ram_progress = QProgressBar()
        self.ram_progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ram_progress.setTextVisible(True)
        self.ram_progress.setMinimumSize(150, 20)
        self.ram_progress.setMaximumSize(300, 20)
        self.ram_usage_label = QLabel("0 / 0 GB")
        ram_layout.addWidget(ram_label)
        ram_layout.addWidget(self.ram_progress)
        ram_layout.addWidget(self.ram_usage_label)
        main_layout.addLayout(ram_layout)

        # Disk Section
        disk_layout = QHBoxLayout()
        disk_label = QLabel("Disk Usage:")
        disk_label.setFont(QFont("Arial", 12))
        self.disk_progress = QProgressBar()
        self.disk_progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.disk_progress.setTextVisible(True)
        self.disk_progress.setMinimumSize(150, 20)
        self.disk_progress.setMaximumSize(300, 20)
        self.disk_usage_label = QLabel("0 / 0 GB")
        disk_layout.addWidget(disk_label)
        disk_layout.addWidget(self.disk_progress)
        disk_layout.addWidget(self.disk_usage_label)
        main_layout.addLayout(disk_layout)

        # Recording and History buttons Layout
        buttons_layout = QVBoxLayout()

        # Recording Section
        recording_layout = QHBoxLayout()
        self.record_button = QPushButton("Start Rec")
        self.record_button.setFixedSize(150, 50)
        recording_layout.addWidget(self.record_button, alignment=Qt.AlignmentFlag.AlignCenter)
        buttons_layout.addLayout(recording_layout)

        # History Button
        self.history_button = QPushButton("Show History")
        self.history_button.setFixedSize(150, 50)
        buttons_layout.addWidget(
            self.history_button, 
            alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addLayout(buttons_layout)

        # Interval Section
        interval_layout = QVBoxLayout()
        interval_row = QHBoxLayout()
        interval_label = QLabel("Interval (sec):")
        self.interval_input = QLineEdit("1")
        self.interval_input.setFixedWidth(60)
        interval_row.addWidget(interval_label, alignment=Qt.AlignmentFlag.AlignCenter)
        interval_row.addWidget(self.interval_input, alignment=Qt.AlignmentFlag.AlignCenter)
        interval_row.setAlignment(Qt.AlignmentFlag.AlignCenter)

        interval_layout.addLayout(interval_row)
        set_interval_button = QPushButton("Set")
        set_interval_button.clicked.connect(self.set_interval)
        set_interval_button.setFixedWidth(150)
        interval_layout.addWidget(set_interval_button, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(interval_layout)

        # Add spacer after widgets to center them vertically
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(main_layout)

        self.history_window = HistoryWindow()
        self.app_logic = AppLogic(self)
        self.record_button.clicked.connect(self.app_logic.switch_recording_text)
        self.history_button.clicked.connect(self.app_logic.open_history_window)

    def set_interval(self):
        try:
            interval = int(self.interval_input.text())*1000
            self.app_logic.set_timer_interval(interval)
        except ValueError:
            print('Please input a number')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())