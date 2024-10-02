import sys
import os
import csv
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class RentCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Set fixed window size and center the window
        self.setFixedSize(400, 500)
        self.center_window()

        # Set window title
        self.setWindowTitle('Rent Calculator')

        # Styling - fonts, colors, padding
        label_font = QFont("Arial", 11)
        input_font = QFont("Arial", 10)
        button_font = QFont("Arial", 11, QFont.Bold)

        # User info fields
        self.name_label = QLabel("Enter your name:", self)
        self.name_label.setFont(label_font)
        self.name_input = QLineEdit(self)
        self.name_input.setFont(input_font)

        self.room_label = QLabel("Enter your room number:", self)
        self.room_label.setFont(label_font)
        self.room_input = QLineEdit(self)
        self.room_input.setFont(input_font)

        # Rent and other costs
        self.rent_label = QLabel("Enter monthly rent amount:", self)
        self.rent_label.setFont(label_font)
        self.rent_input = QLineEdit(self)
        self.rent_input.setFont(input_font)

        self.months_label = QLabel("Enter number of months:", self)
        self.months_label.setFont(label_font)
        self.months_input = QLineEdit(self)
        self.months_input.setFont(input_font)

        self.food_label = QLabel("Enter monthly food cost:", self)
        self.food_label.setFont(label_font)
        self.food_input = QLineEdit(self)
        self.food_input.setFont(input_font)

        self.laundry_label = QLabel("Enter monthly laundry cost:", self)
        self.laundry_label.setFont(label_font)
        self.laundry_input = QLineEdit(self)
        self.laundry_input.setFont(input_font)

        self.maintenance_label = QLabel("Enter monthly maintenance cost:", self)
        self.maintenance_label.setFont(label_font)
        self.maintenance_input = QLineEdit(self)
        self.maintenance_input.setFont(input_font)

        self.electricity_label = QLabel("Enter monthly electricity charge:", self)
        self.electricity_label.setFont(label_font)
        self.electricity_input = QLineEdit(self)
        self.electricity_input.setFont(input_font)

        # Calculate and Save buttons
        self.calculate_button = QPushButton("Calculate Rent", self)
        self.calculate_button.setFont(button_font)
        self.calculate_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
        self.calculate_button.clicked.connect(self.calculate_rent)

        self.save_button = QPushButton("Save to CSV", self)
        self.save_button.setFont(button_font)
        self.save_button.setStyleSheet("background-color: #2196F3; color: white; padding: 10px;")
        self.save_button.clicked.connect(self.save_to_csv)

        # Set layout
        layout = QVBoxLayout()
        layout.setSpacing(10)  # Adds spacing between elements

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.room_label)
        layout.addWidget(self.room_input)
        layout.addWidget(self.rent_label)
        layout.addWidget(self.rent_input)
        layout.addWidget(self.months_label)
        layout.addWidget(self.months_input)
        layout.addWidget(self.food_label)
        layout.addWidget(self.food_input)
        layout.addWidget(self.laundry_label)
        layout.addWidget(self.laundry_input)
        layout.addWidget(self.maintenance_label)
        layout.addWidget(self.maintenance_input)
        layout.addWidget(self.electricity_label)
        layout.addWidget(self.electricity_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.save_button)
        
        self.setLayout(layout)
        self.show()
    
    def center_window(self):
        # Method to center the window
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def calculate_rent(self):
        try:
            rent_amount = float(self.rent_input.text())
            months = int(self.months_input.text())
            food_cost = float(self.food_input.text())
            laundry_cost = float(self.laundry_input.text())
            maintenance_cost = float(self.maintenance_input.text())
            electricity_cost = float(self.electricity_input.text())
            
            # Calculate total costs
            total_rent = rent_amount * months
            total_food = food_cost * months
            total_laundry = laundry_cost * months
            total_maintenance = maintenance_cost * months
            total_electricity = electricity_cost * months
            grand_total = total_rent + total_food + total_laundry + total_maintenance + total_electricity
            
            # Display the result in a message box
            QMessageBox.information(self, 'Total Cost', 
                f'Total Rent: ₹{total_rent}\n'
                f'Total Food Cost: ₹{total_food}\n'
                f'Total Laundry Cost: ₹{total_laundry}\n'
                f'Total Maintenance Cost: ₹{total_maintenance}\n'
                f'Total Electricity Charge: ₹{total_electricity}\n\n'
                f'Grand Total: ₹{grand_total}')
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numeric values.')
    
    def save_to_csv(self):
        try:
            # Get user details
            user_name = self.name_input.text().strip()
            room_number = self.room_input.text().strip()
            
            if not user_name or not room_number:
                QMessageBox.warning(self, 'Input Error', 'Please enter your name and room number.')
                return
            
            # Rent and other costs
            rent_amount = float(self.rent_input.text())
            months = int(self.months_input.text())
            food_cost = float(self.food_input.text())
            laundry_cost = float(self.laundry_input.text())
            maintenance_cost = float(self.maintenance_input.text())
            electricity_cost = float(self.electricity_input.text())
            
            # Calculate totals
            total_rent = rent_amount * months
            total_food = food_cost * months
            total_laundry = laundry_cost * months
            total_maintenance = maintenance_cost * months
            total_electricity = electricity_cost * months
            grand_total = total_rent + total_food + total_laundry + total_maintenance + total_electricity

            # Generate a random 5-digit month number
            random_month_number = random.randint(10000, 99999)
            
            # Create a folder for the user if it doesn't exist
            folder_path = os.path.join(os.getcwd(), user_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Construct the CSV file name with room number and random month number
            file_name = f"{user_name}_Room{room_number}_Month{random_month_number}.csv"
            file_path = os.path.join(folder_path, file_name)
            
            # Write to CSV
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Category", "Monthly Cost", "Total Cost"])
                writer.writerow(["Rent", rent_amount, total_rent])
                writer.writerow(["Food", food_cost, total_food])
                writer.writerow(["Laundry", laundry_cost, total_laundry])
                writer.writerow(["Maintenance", maintenance_cost, total_maintenance])
                writer.writerow(["Electricity", electricity_cost, total_electricity])
                writer.writerow(["Grand Total", "", grand_total])
            
            QMessageBox.information(self, 'File Saved', f'Data saved successfully in {file_path}')
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numeric values before saving.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = RentCalculator()
    sys.exit(app.exec_())
