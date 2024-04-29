import requests
from temporary.bs4 import BeautifulSoup
import time
import random

# Function to scrape title, price, and discount from Amazon
def scrape_amazon_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        # Send GET request with headers
        response = requests.get(url, headers=headers)
        # If request is successful, parse the HTML
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the title element
            title_element = soup.find('span', {'id': 'productTitle'})
            if title_element:
                # Extract the title
                title = title_element.get_text().strip()
            else:
                title = "Title not found"
            
            # Find the price element
            price_element = soup.find('span', {'class': 'a-price-whole'})
            if price_element:
                # Extract the price
                price = price_element.get_text().strip()
            else:
                price = "Price not found"

            # Find the discount element
            discount_element = soup.find('span', {'class': 'savingsPercentage'})
            if discount_element:
                # Extract the discount
                discount = discount_element.get_text().strip()
            else:
                discount = "Discount not found"
            
            mrp_element = soup.find('span', {'class': 'a-text-price'})
            if mrp_element:
                # Extract the discount
                mrp = mrp = mrp_element.find('span', {'class': 'a-offscreen'}).text.strip()
            else:
                mrp = "MRP not found"

            return title, price, discount, mrp
        else:
            print("Failed to fetch page:", response.status_code)
            return None, None, None
    except Exception as e:
        print("Error occurred:", e)
        return None, None, None

# URL of the Amazon product page
url = 'https://www.amazon.in/realme-Storage-Dimensity-Chipset-Flagship/dp/B0CW61C6LK/ref=sr_1_8?dib=eyJ2IjoiMSJ9.Q5ot89BvHpN6yz9qNXOeIlhWeVY-EaUMBtuZRGxByFJYpZHGSe9ewQd6ucLCZa5RY8b3RIxDfIYpPnK9bLcL7VYl0AGvaHkteHkYeYymvo5t5dwmjLCeO_R9GIQ5yl4Z.1OLZoxlK7ftzmbUXQJumB3BO-_F96hE3_X26fD_w8QY&dib_tag=se&qid=1714315365&rnid=976420031&s=electronics&sr=1-8'

# Scrape title, price, and discount function with delay and user-agent rotation
def scrape_with_delay(url):
    try:
        # Scrape title, price, and discount
        title, price, discount, mrp = scrape_amazon_data(url)
        if title and price and discount:
            print("Title:", title)
            print("Price:", price)
            print("Discount:", discount)
            print("MRP:", mrp)
        else:
            print("Failed to retrieve title, price, or discount")

        # Sleep for a random interval to mimic human behavior
        time.sleep(random.uniform(2, 5))
    except KeyboardInterrupt:
        print("Scraping interrupted by user")

# Execute scraping function with delay and user-agent rotation
scrape_with_delay(url)
