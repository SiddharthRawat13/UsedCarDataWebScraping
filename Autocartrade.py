import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

try:
    data = []

    # Function to extract additional details from the description page
    def extract_description_data(url):
        # Send request to the URL and parse the HTML content
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        
        # Find the container containing the details
        container = soup.find('div', class_="text-left")

        if container:
            # Find all the boxes containing details like engine, average, and transmission
            boxes = container.find_all('ul', class_="list columns columns-1 columns-sm-1 columns-md-2 columns-lg-2 padding-0")
            
            for box in boxes:
                # Extract engine details
                eng = box.find_all('div', class_='display-flex col-xs-10 margin-bottom-0')
                try:
                    engine = eng[1].text.strip()
                except IndexError:
                    engine = 'N/A'

                # Extract average details
                avg = box.find_all('div', class_='display-flex col-xs-10 margin-bottom-0')
                try:
                    average = avg[2].text.strip()
                except IndexError:
                    average = 'N/A'

                # Extract transmission details
                trans = box.find_all('div', class_='display-flex col-xs-10 margin-bottom-0')
                try:
                    transmission = trans[5].text.strip()
                except IndexError:
                    transmission = 'N/A'

                # Print the extracted details
                print("Engine:", engine)
                print("Average:", average)
                print("Transmission:", transmission)
                print('-' * 30) 

                # Uncomment the line below to append the additional data to the last dictionary in the data list
                # data[-1].update({'Engine': engine, 'Average': average, 'Transmission': transmission})
        else:
            print("Container not found.")

    # Base URL and number of pages to scrape
    base_url = "https://www.autotrader.com/cars-for-sale/berlin-md"
    num_pages = 2

    # Loop through each page to scrape car details
    for current_page in range(1, num_pages + 1):
        url = f"{base_url}?page={current_page}"
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        # Find the container containing car details
        car_container = soup.find('div', class_="row display-flex flex-wrap margin-top-3")

        # Loop through each car to extract details
        for car_main in car_container:
            names = car_main.find_all('h2', class_="text-bold text-size-400 link-unstyled")

            for name in names:
                # Extract car name and year
                car_name = name.text if name else "N/A"
                year_match = re.search(r'\b\d{4}\b', car_name)
                year = year_match.group() if year_match else None
                car_name = re.sub(r'\b\d{4}\b', '', car_name).strip()

                # Extract car price and miles
                price = car_main.find('div', class_="text-size-600 text-ultra-bold first-price").text.strip()
                mile = car_main.find('div', class_="text-bold text-subdued-lighter").text.strip()

                # Print basic car details
                print("Name:", car_name)
                print("Year:", year)
                print("Price:", price)
                print("Miles:", mile)
                #print('*' * 30)

                # Extract URL for description page
                link = name.find_parent('a')['href']
                url_description = "https://www.autotrader.com" + link
                
                # Uncomment the line below to append basic car details to the data list
                # data.append({'Name': car_name, 'Year': year, 'Price': price, 'Miles': mile})
                
                # Call function to extract additional details from the description page
                extract_description_data(url_description)

    # Create DataFrame from collected data
    # df = pd.DataFrame(data)
    
    # Save DataFrame to CSV file
    # df.to_csv('C:/Users/LENOVO/OneDrive/Desktop/python/webscraping/car_data2.csv', index=False)

except Exception as e:
    print(e)


