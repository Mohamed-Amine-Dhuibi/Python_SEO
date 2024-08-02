import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

class GoogleSearchSpiderSpider(scrapy.Spider):
    def __init__(self,keyword,id,server ):
        pass
    
    def parse(self, response):
        pass



def run(keyword,id,server): 
    process = CrawlerProcess(get_project_settings())
    spider = GoogleSearchSpiderSpider(keyword,id,server)
    pipeline = MyPipeline()
    process.crawl(spider)
    process.start()
    scraped_data = pipeline.items
    return scraped_data