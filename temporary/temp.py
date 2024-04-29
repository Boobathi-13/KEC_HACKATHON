# import scrapy
# import json

# class AmazonSpider(scrapy.Spider):
#     name = 'amazon_spider'
#     allowed_domains = ['amazon.in']

#     start_urls = [
#         'https://www.amazon.in/crocs-Literide-Unisex-Clog-206708-4CC/dp/B0BWHYVZ53/?_encoding=UTF8&pd_rd_w=LB7x9&content-id=amzn1.sym.4d5b78c6-4f80-4b93-8d16-deb7aaa19e3f%3Aamzn1.symc.afd86303-4a72-4e34-8f6b-19828329e602&pf_rd_p=4d5b78c6-4f80-4b93-8d16-deb7aaa19e3f&pf_rd_r=Q64RYWEVJCGXJHSE1RC5&pd_rd_wg=S6w3G&pd_rd_r=b8b2e978-6127-440c-8a41-f0d1c82588e8&ref_=pd_gw_ci_mcx_mr_hp_atf_m'
#     ]

#     def parse(self, response):
#         original_price = response.css('span.a-price-whole::text').get().strip()

#         data = {
#             'original_price': original_price,
#         }

#         with open('output.json', 'w') as f:
#             json.dump(data, f)



# import scrapy
# import json
# from urllib.parse import urlparse, parse_qs

# class AmazonSpider(scrapy.Spider):
#     name = 'amazon_spider'
#     allowed_domains = ['amazon.in']

#     def start_requests(self):
#         urls = [
#             'https://www.amazon.in/Sounce-Generation-Silicone-Shock-Absorbing-Protective/dp/B0C787PC6J/?_encoding=UTF8&pd_rd_w=UJpAP&content-id=amzn1.sym.842eeae7-088b-4dcc-abf4-f922215eb637&pf_rd_p=842eeae7-088b-4dcc-abf4-f922215eb637&pf_rd_r=DVGYS13G32JWES64KW5P&pd_rd_wg=YQbXZ&pd_rd_r=893bf062-ffe6-402d-826e-e8229cf3847a&ref_=pd_gw_dealz_cs_t1&th=1'
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         # Extracting the long-form URL
#         long_url = self.get_long_url(response.url)

#         original_price = response.css('span.a-price-whole::text').get().strip()

#         data = {
#             'original_price': original_price,
#             'url': long_url
#         }

#         with open('output.json', 'w') as f:
#             json.dump(data, f)

#     def get_long_url(self, url):
#         # Parsing the URL
#         parsed_url = urlparse(url)

#         # Extracting query parameters
#         query_params = parse_qs(parsed_url.query)

#         # Constructing the long-form URL
#         long_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

#         if query_params:
#             long_url += '?' + '&'.join([f'{key}={value[0]}' for key, value in query_params.items()])

#         return long_url


import scrapy
import json
from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message
from scrapy.utils.httpobj import urlparse_cached
from scrapy.utils.python import global_object_name

class Amazon503RetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        return response

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.in']
    start_urls = [
        'https://www.amazon.in/crocs-Unisex-Adult-LiteRide-Clog-Pepper/dp/B0B4SCCNKF/ref=sr_1_8?keywords=crocs+literide+m9w11&qid=1707983458&sr=8-8',
        'https://www.amazon.in/Fire-Boltt-Bluetooth-Calling-Assistance-Resolution/dp/B0BF4YBLPX/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=kmvVt&content-id=amzn1.sym.88f5e114-4865-4b45-bb89-266ae814dfc2%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=88f5e114-4865-4b45-bb89-266ae814dfc2&pf_rd_r=B2131XXMWZRFHAK8VKMF&pd_rd_wg=J7Vo4&pd_rd_r=06d9a79a-2de7-4e2c-a650-1582ec39a4d3&pd_rd_i=B0BF4YBLPX&th=1'
    ]
    
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
            'amazon_scraper.Amazon503RetryMiddleware': 550,
        }
    }

    def parse(self, response):
        price = response.css('.a-price-whole::text').get().strip()

        data = {
            'url': response.url,
            'price': price
        }

        with open('output.json', 'a') as f:
            json.dump(data, f)
            f.write('\n')

# Run the spider
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess()
    process.crawl(AmazonSpider)
    process.start()
