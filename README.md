# Web Scraping Car Data from AutoTrader
"Web scraping of used car data from AutoTrader using Python. This project involves scraping car details like name, year, price, mileage, engine size, etc., from the AutoTrader website. The scraped data is then used for data analysis, cleaning, and exploratory data analysis. Implemented using Python libraries like BeautifulSoup and Pandas."

## Overview
This Python script is designed to scrape car data from the AutoTrader website. It extracts information such as car name, year, price, and miles from the main listings page. Additionally, it navigates to the individual car description pages to gather more details like engine type, average consumption, and transmission.

### Requirements
Python 3.x,
pandas,
requests,
BeautifulSoup,
re
### Installation
pip install pandas ,requests, beautifulsoup4
### Usage
Open the Python script scrape_cars.py.
Modify the base_url and num_pages variables to specify the AutoTrader listings page and the number of pages to scrape.
Run the script using the command:

python scrape_cars.py
The script will print the extracted car details and additional data from the description pages.
### Description
extract_description_data(url)
This function extracts additional details like engine type, average consumption, and transmission from the individual car description pages.

Engine: Type of engine (e.g., V6, 4-cylinder)
Average: Average fuel consumption
Transmission: Transmission type (e.g., automatic, manual)
### Main Script Execution
The script starts by specifying the base_url and num_pages to scrape.
It loops through each page to extract car details such as name, year, price, and miles.
For each car, it navigates to the description page to call extract_description_data() and gather additional details.
The collected data can be appended to a list or saved to a CSV file using pandas DataFrame.
### Data Storage
The script has a commented-out section to save the collected data to a CSV file named car_data2.csv. Uncomment the relevant lines to enable this feature.

### Error Handling
The script includes basic error handling to manage exceptions that may occur during web scraping.






