import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
