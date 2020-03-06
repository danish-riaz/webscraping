# -*- coding: utf-8 -*-
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
from scrapy import Spider
# from selenium import webdriver
# from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from book_crawler.items import BookCrawlerItem


def get_table_data(response, name):
    return response.xpath('//th[text()="' + name + '"]/following-sibling::td/text()').extract_first()


class CrawlSpider(Spider):
    name = 'crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ('http://books.toscrape.com/',)

    # def __init__(self, category):
    #     self.start_urls = [category]

    def parse(self, response):
        books = response.xpath("//h3/a/@href").extract()
        for book in books:
            book_url = response.urljoin(book)
            yield Request(book_url, callback=self.each_book)
        # next_page = response.xpath(
        #     "//*[@class='next']/a[text()='next']/@href").extract_first()
        # next_page_url = response.urljoin(next_page)
        # yield Request(next_page_url)

    def each_book(self, response):
        item_loader_obj = ItemLoader(
            item=BookCrawlerItem(), response=response)
        h1 = response.xpath(
            "//*[@class='col-sm-6 product_main']/h1/text()").extract_first()
        price = response.xpath(
            "//*[@class='price_color']/text()").extract_first()

        rating = response.xpath(
            ".//*[contains(@class, 'star-rating')]/@class").extract_first()
        rating = rating.replace('star-rating ', '')

        image_urls = response.xpath(
            "//*[@class='item active']/img/@src").extract_first()
        image_urls = image_urls.replace('../../', 'http://books.toscrape.com/')

        des = response.xpath(
            "//*[@id='product_description']/following-sibling::p/text()").extract_first()

        upc = get_table_data(response, "UPC")
        product_type = get_table_data(response, "Product Type")
        price_etax = get_table_data(response, "Price (excl. tax)")
        price_itac = get_table_data(response, "Price (incl. tax)")
        tax = get_table_data(response, "Tax")
        avalibility = get_table_data(response, "Availability")
        reviews = get_table_data(response, "Number of reviews")

        item_loader_obj.add_value('h1', h1)
        item_loader_obj.add_value('price', price)
        item_loader_obj.add_value('rating', rating)
        item_loader_obj.add_value('image_urls', image_urls)
        item_loader_obj.add_value('upc', upc)
        item_loader_obj.add_value('product_type', product_type)
        item_loader_obj.add_value('price_etax', price_etax)
        item_loader_obj.add_value('price_itac', price_itac)
        item_loader_obj.add_value('tax', tax)
        item_loader_obj.add_value('avalibility', avalibility)
        item_loader_obj.add_value('reviews', reviews)
        item_loader_obj.add_value('des', des)

        return item_loader_obj.load_item()
        # yield{'Heading': h1,
        #       'Price': price,
        #       'Rating': rating,
        #       'Image': image_urls,
        #       'UPC': upc,
        #       'Product Type': product_type,
        #       'Price (excl. tax)': price_etax,
        #       'Price (incl. tax)': price_itac,
        #       'Tax': tax,
        #       'Availability': avalibility,
        #       'Number of reviews': reviews,
        #       'Description': des, }
        # def start_requests(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://books.toscrape.com/')

    #     sel = Selector(text=self.driver.page_source)
    #     books = sel.xpath("//h3/a/@href").extract()
    #     for book in books:
    #         book_url = 'http://books.toscrape.com/' + book
    #         yield Request(book_url, callback=self.parse_book)

    # def parse_book(self, response):
    #     pass

    # start_urls = ['http://books.toscrape.com/']

    # # rule = (Rule(LinkExtractor(deny_domains='google.com'),
    # #         callback='book_crawl', follow=True),)
    # rule = (Rule(LinkExtractor(allow='music'),
    #              callback='book_crawl', follow=True))

    # def parse(self, response):
    #     pass

    # def book_crawl(self, response):
    #     yield {
    #         'URL': response.url
    #     }
