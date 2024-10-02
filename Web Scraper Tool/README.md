# Web Scraper Tool

### Developed by Dev Kumar | Internship Project at Hex Software

This project is a **Web Scraper Tool** built with Python and PyQt5. It allows users to input a website URL and extract various types of data from the webpage, including contact information, embedded links, technical details, and more. The scraped data can also be saved in a CSV format.

## Features

- **Author Information**: Scrapes author details from webpage metadata.
- **Contact Information**: Extracts email addresses and phone numbers from the page.
- **Embedded Links**: Identifies and categorizes internal and external links.
- **Address Detection**: Tries to detect addresses on the webpage.
- **Technical Details**: Extracts programming language, web server information, and open ports using Nmap.
- **Form and File Upload Information**: Detects input fields and file upload mechanisms on the page.
- **Save to CSV**: The scraped data can be saved in a CSV format for further analysis.

## Requirements

- Python 3.x
- PyQt5 (`pip install pyqt5`)
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)
- Nmap (for port scanning functionality)
- CSV module (built-in with Python)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/devkumar-swipe/hex_software/web-scraper-tool.git
    cd web-scraper-tool
    ```

2. **Install the required dependencies**:
    ```bash
    pip install pyqt5 beautifulsoup4 requests
    ```

3. **Ensure Nmap is installed**:
    - Linux: Install via the package manager (`sudo apt-get install nmap`).
    - Windows: Download and install from the [Nmap website](https://nmap.org/download.html).

## Usage

1. Run the application:
    ```bash
    python scraper.py
    ```

2. Input the website URL in the provided text field (e.g., `https://example.com`).

3. Click **Scrape Data** to extract the information from the webpage.

4. View the extracted data in the output area.

5. Save the data to a CSV file by clicking **Save to CSV**.

## review
1. feel free to contact me for any changes 
devkumar@cyberswipe.in
