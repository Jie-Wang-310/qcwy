# -*- coding: utf-8 -*-
import scrapy
from qcwy.items import QcwyItem
from scrapy.http import Request


class MainSpider(scrapy.Spider):
    name = 'main'
    # allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html']


    # 生成要抓取的页面地址，从1-723页
    '''
    如果说通过获取下一页链接回调参数不能成功，可以采取自己生成页面链接的方式进行爬取内容
    '''
    def start_requests(self):
        pages = []
        for i in range(1, 724):
            newpage = scrapy.Request('https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,%d.html' %i)
            pages = newpage
            yield pages

    def parse(self, response):
        print(response.body)
        item = QcwyItem()
        jobs = response.xpath('//div[@class="el"]')
        for job in jobs:
            job_name = job.xpath('p/span/a/@title').extract_first()
            company = job.xpath('span/a/@title').extract_first()
            area = job.xpath('span[@class="t3"]/text()').extract()
            salary = job.xpath('span[@class="t4"]/text()').extract()
            pabulish_time = job.xpath('span[@class="t5"]/text()').extract()
            item['job_name'] = job_name
            item['company'] = company
            item['area'] = area
            item['salary'] = salary
            item['pabulish_time'] = pabulish_time
            yield item

        '''
        如果说下一页链接是可以调用，或者说拼接成新链接形式的，可以使用这种方法
        '''
            # nextpage = response.xpath('//ul/li[@class="bk"]/a/@href').extract()
            # url = nextpage   # 直接调用
            # url urljoin(nextpage)  # 链接拼接的形式
            # # print(url)
            # yield scrapy.Request(url=url, callback=self.parse)































