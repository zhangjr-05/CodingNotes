import scrapy


class GetMovieSpider(scrapy.Spider):
    name = "get_movie"
    allowed_domains = ["www.maoyan.com"]
    start_urls = ["https://www.maoyan.com/board/4"]

    def parse(self, response):
        pass
