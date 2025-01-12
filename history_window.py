from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QHeaderView, QTableWidgetItem
)
from PySide6.QtCore import Qt


class HistoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("History")
        self.setGeometry(200, 200, 800, 400)

        main_layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(9)  # Изменили количество столбцов на 9
        self.table.setHorizontalHeaderLabels([
            "ID", "CPU %", "RAM %", "RAM Used (GB)",
            "RAM Total (GB)", "Disk %", "Disk Used (GB)", "Disk Total (GB)",
            "Recording Time"  # Добавили столбец "Recording Time"
        ])

        # Настройка размера колонок
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

    def set_data(self, data):
        self.table.setRowCount(len(data))
        for row, record in enumerate(data):
            for col, value in enumerate(record):
                if isinstance(value, float) and col != 8:
                    item = f"{value:.2f}"
                else:
                    item = str(value)
                self.table.setItem(row, col, QTableWidgetItem(item))
