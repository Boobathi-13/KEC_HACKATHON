# import requests
# from bs4 import BeautifulSoup

# # Function to scrape title, price, and discount from Amazon
# def scrape_amazon_data(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     try:
#         # Send GET request with headers
#         response = requests.get(url, headers=headers)
#         # If request is successful, parse the HTML
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             # Find the title element
#             title_element = soup.find('span', {'id': 'productTitle'})
#             if title_element:
#                 # Extract the title
#                 title = title_element.get_text().strip()
#             else:
#                 title = "Title not found"
            
#             # Find the price element
#             price_element = soup.find('span', {'class': 'a-price-whole'})
#             if price_element:
#                 # Extract the price
#                 price = price_element.get_text().strip()
#             else:
#                 price = "Price not found"

#             # Find the discount element
#             discount_element = soup.find('span', {'class': 'savingsPercentage'})
#             if discount_element:
#                 # Extract the discount
#                 discount = discount_element.get_text().strip()
#             else:
#                 discount = "Discount not found"
            
#             # Find the MRP element
#             mrp_element = soup.find('span', {'class': 'a-text-price'})
#             if mrp_element:
#                 # Extract the MRP
#                 mrp = mrp_element.find('span', {'class': 'a-offscreen'}).text.strip()
#             else:
#                 mrp = "MRP not found"

#             return title, price, discount, mrp
#         else:
#             print("Failed to fetch page:", response.status_code)
#             return None, None, None
#     except Exception as e:
#         print("Error occurred:", e)
#         return None, None, None
