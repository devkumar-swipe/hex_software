import sys
import phonenumbers
import folium
from opencage.geocoder import OpenCageGeocode
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

class GeolocationTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Create widgets
        self.api_key_label = QLabel("Enter OpenCage API Key:", self)
        self.api_key_input = QLineEdit(self)
        
        self.country_code_label = QLabel("Enter Country Code:", self)
        self.country_code_input = QLineEdit(self)
        
        self.number_label = QLabel("Enter Phone Number:", self)
        self.number_input = QLineEdit(self)
        
        self.track_button = QPushButton("Track Geolocation", self)
        self.track_button.clicked.connect(self.track_geolocation)
        
        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.api_key_label)
        layout.addWidget(self.api_key_input)
        layout.addWidget(self.country_code_label)
        layout.addWidget(self.country_code_input)
        layout.addWidget(self.number_label)
        layout.addWidget(self.number_input)
        layout.addWidget(self.track_button)
        
        self.setLayout(layout)
        self.setWindowTitle('Geolocation Tracker')
        self.setGeometry(300, 300, 300, 250)  # Set the window size
        self.show()

    def track_geolocation(self):
        # Get user input
        api_key = self.api_key_input.text().strip()
        country_code = self.country_code_input.text().strip()
        phone_number = self.number_input.text().strip()

        if not api_key or not country_code or not phone_number:
            QMessageBox.warning(self, 'Input Error', 'Please enter all fields: API Key, Country Code, and Phone Number.')
            return

        full_number = f"+{country_code}{phone_number}"
        
        # Step 1: Parse phone number and get location
        try:
            pepnumber = phonenumbers.parse(full_number)
            location = phonenumbers.geocoder.description_for_number(pepnumber, "en")
            carrier_name = phonenumbers.carrier.name_for_number(pepnumber, "en")
            
            # Step 2: Use OpenCage to get coordinates for the location
            geocoder = OpenCageGeocode(api_key)
            query = str(location)
            result = geocoder.geocode(query)
            
            if result:
                lat = result[0]['geometry']['lat']
                lng = result[0]['geometry']['lng']
                
                # Step 3: Display location on a map using folium
                my_map = folium.Map(location=[lat, lng], zoom_start=9)
                folium.Marker([lat, lng], popup=f"{location} ({carrier_name})").add_to(my_map)
                
                # Save the map to an HTML file
                map_file = "geolocation_map.html"
                my_map.save(map_file)
                
                QMessageBox.information(self, 'Geolocation Result', f"Location: {location}\nCarrier: {carrier_name}\nMap saved as '{map_file}'")
            else:
                QMessageBox.warning(self, 'Geolocation Error', 'Could not retrieve geolocation data.')
        except phonenumbers.NumberParseException as e:
            QMessageBox.warning(self, 'Input Error', f"Invalid phone number: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tracker = GeolocationTracker()
    sys.exit(app.exec_())
