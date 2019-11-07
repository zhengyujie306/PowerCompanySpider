import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re,time
class BselSpider(CrawlSpider):
    name = 'bs'
    start_urls = ['http://www.sgcc.com.cn','http://www.eptchina.com']
    #规则：将需要点击的网址按规则一条一条写入，以下规则写入两条，一条是标题栏以及翻页的信息，一条是商品信息，并调用回调函数parse_item，这里来简单的，进行源码保存
    rules=(
            Rule(LinkExtractor(allow=r'http://www.[a-zA-Z0-9\.\/]+'),callback='parse_item', follow=True),
        #不需要回调函数 因为规则可以做到
        #Rule(LinkExtractor(allow=r'http://www.bsriceones.ga/[a-zA-Z0-9-]+/'),follow=True),
        #Rule(LinkExtractor(allow=r'http://www.bsriceones.ga/[a-zA-Z0-9-]+/.*page=\d+'), follow=True),
    )
    def parse_item(self, response):
        #html_name = re.findall(r'http://www.\d+',response
        print("-------------------------------------")
        print(response.url)
        yield{'link':response.url,}
       # print(html_name)
        print("-------------------------------------")
        with open("/home/zhengyujie/bsriceones/html/"+response.url.replace('/',':')+".html",'wb') as f:
            f.write(response.body) 
