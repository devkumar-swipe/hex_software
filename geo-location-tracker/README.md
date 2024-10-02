# Geolocation Tracker

### Developed by Dev Kumar | Internship Project at Hex Software

The **Geolocation Tracker** is a desktop application built using Python and PyQt5 that tracks the location of a phone number based on its country code and phone number. It uses the OpenCage Geocoding API to fetch coordinates and display the location on a map using the **folium** library.

## Features

- **Track Phone Number Location**: Users can input a phone number and its country code to get the location associated with the number.
- **Carrier Information**: The app also fetches the carrier (network provider) associated with the phone number.
- **Map Visualization**: The location is displayed on an interactive map using **folium**, which is saved as an HTML file.
  
## Requirements

- Python 3.x
- PyQt5 (`pip install pyqt5`)
- phonenumbers (`pip install phonenumbers`)
- folium (`pip install folium`)
- OpenCage Geocoding API Key (Free Registration)

## OpenCage API Setup

1. **Register on OpenCage**:  
   Visit the [OpenCage Geocoding website](https://opencagedata.com/) and create a free account.
   
2. **Get API Key**:  
   Once registered, log in to your OpenCage account and generate an API key from the dashboard. You will need this key to use the geolocation services in the application.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/devkumar-swipe/hex_software/geolocation-tracker.git
    cd geolocation-tracker
    ```

2. **Install the required dependencies**:
    ```bash
    pip install pyqt5 phonenumbers folium opencage
    ```

## Usage

1. Run the application:
    ```bash
    python geolocation_tracker.py
    ```

2. In the application window:
    - Enter your **OpenCage API Key** (get it from the OpenCage Geocoding website as described above).
    - Enter the **Country Code** for the phone number (e.g., 1 for the US, 91 for India).
    - Enter the **Phone Number** without the country code (e.g., 1234567890).

3. Click **Track Geolocation** to fetch the location and carrier information.

4. The result will show:
    - **Location**: The general region or area associated with the phone number.
    - **Carrier**: The network provider of the phone number.
    - **Map**: An HTML file named `geolocation_map.html` will be generated and saved in the current directory, showing the location on a map.

## Info
feel free to ask any doubts 
devkumar@cyberswipe.in
