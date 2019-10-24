# -*- coding: utf-8 -*-
import re
import scrapy
from beer.items import BeerItem
from datetime import timedelta, date
from urllib import parse
import time
import random
from time import sleep


counties_list= ['au','at','be','br','ca','cz','dk','de','fr','ie','it','jp','mx','nl','nz','no','pl','se','gb','us']
url_format = 'https://www.beeradvocate.com/beer/top-rated/{0}'

class BeerSpider(scrapy.Spider):
    name = 'beer'
    start_urls = []

    for counties in counties_list:
        start_urls.append(url_format.format(counties))

    def parse(self, response):
        for href in response.xpath("//*[@id='ba-content']/table/tr/td[2]/a/@href").extract():
            yield response.follow(href, self.parse_details)

    # def parse_details(self, response):
        
    #     re_ct = response.xpath('//*[@id="ba-content"]/div[9]/b/text()').get()
    #     afterct = re.sub('Reviews: ','',re_ct).strip()
    #     afterct2= re.sub(',','',afterct)        
    #     counting = int(afterct2)
    #     pages = (counting//25)+1
    #     new_url = str(response).split(' ')[1][:-1]
    #     for idx in range(0,pages):
    #         if idx == 0:
    #             print('idx==0', new_url)
    #             yield response.follow(new_url, self.parse_details2)
    #         elif idx != pages:
    #             print('idx!=0')
    #             nextpg = response.xpath('//*[@id="ba-content"]/div[8]/span/a/@href').extract()
    #             # print('NEXTTTTTTT', nextpg, len(nextpg))
    #             yield response.follow(nextpg[-2], self.parse_details2)
    #         else:
    #             print('idx == pages')
    #             pass
        # if response.xpath('//*[@id="ba-content"]/div[8]/span/span') == False:
        #     if len(response.xpath('//*[@id="ba-content"]/div[8]/span')) == 
        #     abc = response.xpath('//*[@id="ba-content"]/div[8]/span/a[-2]/@href').get()
        #     yield response.follow(abc, self.parse_details2)

    def parse_details(self, response):
        for idx2 in response.xpath('//*[@id="rating_fullview_content_2"]').extract():
            item = BeerItem()
            re_ct = response.xpath('//*[@id="ba-content"]/div[9]/b/text()').get()
            afterct = re.sub('Reviews: ','',re_ct).strip()
            afterct2= re.sub(',','',afterct)        
            item['review_ct'] = int(afterct2)
            item['name'] = str(response.xpath('//*[@id="content"]/div/div/div[3]/div/div/div[1]/h1/text()').get())
            item['style'] = str(response.xpath('//*[@id="info_box"]/div[2]/dl/dd[1]/a[1]/b/text()').get())
            item['company'] = str(response.xpath('//*[@id="info_box"]/div[2]/dl/dd[7]/a/text()').get())
            item['avg'] = response.xpath('//*[@id="info_box"]/div[2]/dl/dd[4]/b/span/text()').get()
            item['country'] = str(response.xpath('//*[@id="info_box"]/div[2]/dl/dd[8]/a/text()').get())
            item['alcohol']=response.xpath("//*[@id='info_box']/div[2]/dl/dd[2]/span/b/text()").get()
            item['available'] = str(response.xpath("//*[@id='info_box']/div[2]/dl/dd[9]/span/text()").get())
            temp1 = idx2.split('<br><br>')
            item['score'] = temp1[0]
            item['review'] = temp1[1]
            yield item
        try:
            if response.xpath('//*[@id="ba-content"]/div[8]/span/span/text()').get() != 'next → last':
                nextpg = response.xpath('//*[@id="ba-content"]/div[8]/span/a/@href').extract()
                yield response.follow(nextpg[-2], self.parse_details)
        except:
            pass
