import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the website to scrape
url = 'http://books.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    titles = soup.find_all('h3')
    prices = soup.find_all('p', class_='price_color')

    titles_text = [title.get_text() for title in titles]
    prices_text = [price.get_text() for price in prices]

    data = pd.DataFrame({
        'Title': titles_text,
        'Price': prices_text
    })

    # Save the data to a CSV file
    data.to_csv('scraped_books.csv', index=False)

    print('Data has been scraped and saved to scraped_books.csv')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
