import scrapy
import json

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.in']

    start_urls = [
        'https://www.amazon.in/Lava-Dimensity-Processor-FrontCamera-ExpandableRAM/dp/B0CHM729GT/?_encoding=UTF8&pd_rd_w=Gq9fL&content-id=amzn1.sym.f44f52ee-9bb9-4840-ad16-45c5ce2faa4f&pf_rd_p=f44f52ee-9bb9-4840-ad16-45c5ce2faa4f&pf_rd_r=383CRKM41QHXNK8TBVEZ&pd_rd_wg=kA62n&pd_rd_r=76579d99-cf2c-4bc7-ae4f-3da93b18d3da&ref_=pd_gw_dealz_m1_t1&th=1'
    ]

    def parse(self, response):
        title = response.css('span#productTitle::text').get().strip()
        original_price = response.css('span.a-price-whole::text').get().strip()

        data = {
            'title': title,
            'original_price': original_price,
        }

        with open('output.json', 'w') as f:
            json.dump(data, f)