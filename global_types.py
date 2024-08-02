import scrapy
from scrapy.item import Item, Field

class MyScrapyItem(Item):
    link_id=Field()
    link = Field()
    content = Field()
    clean_content=Field()
    headers = Field()
    images = Field()
    content_length=Field()
    header_length=Field()
    nb_p=Field()
    nb_h=Field()
    nb_img=Field()
    nb_h1_img=Field()
    headers_keywords=Field()
    content_keywords=Field()
    keywords_id=Field()
    created_at=Field()

class linkItem(Item):
    link = Field()
    subject=Field()
    keywords_id=Field()



 # type: ignore