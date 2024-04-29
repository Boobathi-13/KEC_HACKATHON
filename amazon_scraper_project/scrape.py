import requests
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent
from scrapingbee import ScrapingBeeClient

# Initialize the ScrapingBee client with your API key
client = ScrapingBeeClient('D8PN1I9CVN7VXFMGXRW62PFO6E7399VLP6V0S2ZZJU448Z3G6TZBIEYCBQXABUGAL1QMZG5UGWAQRVW1')

# Function to generate a random user agent
def get_random_user_agent():
    ua = UserAgent()
    return ua.random

# Function to scrape title, price, and discount from Amazon
def scrape_amazon_data(url):
    # Send GET request with headers and rotating IP address
    response = client.get(url)

    # If request is successful, parse the HTML
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

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

        # Find the MRP element
        mrp_element = soup.find('span', {'class': 'a-text-price'})
        if mrp_element:
            # Extract the MRP
            mrp = mrp_element.find('span', {'class': 'a-offscreen'}).text.strip()
        else:
            mrp = "MRP not found"

        # Add a delay between requests (adjust as needed)
        time.sleep(random.uniform(1, 2))

        return title, price, discount, mrp
    else:
        print("Failed to fetch page:", response.status_code)
        return None, None, None