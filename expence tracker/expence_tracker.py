import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox, QTableWidget, QTableWidgetItem
)

class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Expense Tracker')
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Input fields
        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText('Enter expense amount')
        
        self.category_input = QLineEdit(self)
        self.category_input.setPlaceholderText('Enter expense category')

        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText('Enter date (YYYY-MM-DD)')

        # Buttons
        add_button = QPushButton('Add Expense', self)
        add_button.clicked.connect(self.add_expense)

        # Layout
        layout.addWidget(QLabel('Expense Amount:'))
        layout.addWidget(self.amount_input)
        layout.addWidget(QLabel('Expense Category:'))
        layout.addWidget(self.category_input)
        layout.addWidget(QLabel('Expense Date:'))
        layout.addWidget(self.date_input)
        layout.addWidget(add_button)

        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Amount', 'Category', 'Date'])
        layout.addWidget(self.table)

        self.setLayout(layout)

    def add_expense(self):
        amount = self.amount_input.text()
        category = self.category_input.text()
        date = self.date_input.text()

        if amount and category and date:
            self.save_expense(amount, category, date)
            self.load_expenses()
            self.amount_input.clear()
            self.category_input.clear()
            self.date_input.clear()
        else:
            QMessageBox.warning(self, 'Input Error', 'Please fill all fields.')

    def save_expense(self, amount, category, date):
        with open('expenses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date])

    def load_expenses(self):
        self.table.setRowCount(0)  # Clear previous data
        try:
            with open('expenses.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    for column, data in enumerate(row):
                        self.table.setItem(row_position, column, QTableWidgetItem(data))
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tracker = ExpenseTracker()
    tracker.load_expenses()  # Load existing expenses when the app starts
    tracker.show()
    sys.exit(app.exec_())
