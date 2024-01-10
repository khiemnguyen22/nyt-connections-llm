# pylint: disable=arguments-differ
# pylint: disable=bare-except
import scrapy
import os
import json

class QuotesSpider(scrapy.Spider):
    name = "connect_crawl"

    def start_requests(self):
        urls = ['https://connections.swellgarfo.com/nyt/'+str(x) for x in range(204, 214)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f'nyt_connect_crawler/puzzles/{page}.html'
        # success = (len(response.css('p.noindent::text').getall()) != 0)
        # self.log(f'success: {success}')
        # if success:
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

class Puzzles(scrapy.Spider):
    name = 'puzzle_crawl'
    # start_urls = ['http://bulletin.iit.edu/undergraduate/courses/cs/']
    start_urls = [f'file:///{os.path.dirname(os.path.dirname(os.path.abspath(__name__)))}/nyt_connect_crawler/nyt_connect_crawler/puzzles/{c}' for c in os.listdir('nyt_connect_crawler/puzzles')]

    def parse(self, response):

        data = response.css('script::text').get()
        parsed_content = json.loads(data)

        # try:
        yield {
            'puzzle_id': parsed_content['props']['pageProps']['id'],
            'content': parsed_content['props']['pageProps']['answers']
        }
        