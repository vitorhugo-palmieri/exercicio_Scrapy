from ast import parse
from gc import callbacks
import scrapy




class WebscraperSpider(scrapy.Spider):
    name = 'webscraper'
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static/computers/laptops']
    contapag=1
    def parse(self, response):
        
        for item in response.xpath("*//div[@class='thumbnail']") :
            
            yield{
                
                
                'name':item.xpath(".//a/@title").get(),
                'price':item.xpath('.//h4[@class="pull-right price"]/text()').get(),
                'description':item.xpath('.//p[@class="description"]/text()').get(),
                'stars': item.xpath('.//p/@data-rating').get()
                
                
            }
            
        #para captar proxima pagina
        tamanho = len(response.css('.page-item').getall())
        prox_pag = response.xpath(f"/html/body/div[1]/div[3]/div/div[2]/ul/li[{tamanho}]/a").attrib['href'] 
        if prox_pag is not None:
            yield scrapy.Request(response.urljoin(prox_pag),callback=self.parse)


        