import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

class ExtractKeyword(scrapy.Spider):
    name = "links"
    _use_scraperapi = True

    def __init__(self,keyword,id,server ):
        super(ExtractKeyword, self).__init__(*args, **kwargs)
        self.model_name = 'sentence-transformers/bert-base-nli-mean-tokens'
        self.tokenizer = BertTokenizer.from_pretrained(self.model_name)
        self.model = BertModel.from_pretrained(self.model_name)

        self.conn = SQLPipeline().conn

        self.cnx = mysql.connector.connect(user='root', password='mariadb',
                                          host='localhost', database='hacktheseo')
        self.cursor = self.cnx.cursor()
        self.content_keywords = []
        self.id = 0

        self.key = keyword
        self.logger.info('keyword: %s', self.key)
        self.language = self.get_language(self.key)
        self.logger.info('langue: %s', self.language)

    
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