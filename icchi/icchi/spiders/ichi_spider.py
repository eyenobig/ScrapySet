import scrapy
# import json
import time
import requests
# import sqlite3
# import os
# from Duelyst.items import DuelystItem

class ichiSpider(scrapy.Spider):
    name = "icchi"
    start_urls = [
        "http://icchibanketu.wikiru.jp/index.php?%B1%D1%B7%E6%2F%A5%C6%A1%BC%A5%D6%A5%EB",
     ]
    i = "阿斯达"
    def parse(self, response):
        listurl = response.xpath('//*[@id="sortabletable1"]/tbody/tr/td[4]/a/@href').extract()
        # print(len(listurl))

        for x in listurl:
            # wikiru采用0.3秒不能连开同网页 做了一点傻瓜调整
            yield scrapy.Request(x,callback=self.parse_content)
            time.sleep(0.4)


        #         yield scrapy.Request(x,callback=self.parse_content)
            # yield scrapy.Request(x,callback=self.parse_content)
        # item = DuelystItem()
        # resp = requests.get('http://www.bagoum.com/cardsFullList', proxies=dict(http='socks5://127.0.0.1:1080',https='socks5://127.0.0.1:1080'))
        # Datalist = resp.json()
        # # 测试用
        # cx = sqlite3.connect(os.getcwd() + "\Duelyst.sqlite")
        # cu = cx.cursor()
        # tablesql = "select * from image"
        # try:
        #     cu.execute(tablesql)
        #     deletetable(cx,cu)
        #     createtable(cx,cu)
        # except sqlite3.OperationalError:
        #     createtable(cx,cu)
        # # tablesql = "create table "+Tname+" ("
        # url = "http://www.bagoum.com/cards/" + Datalist[0].replace(" ","")


        # yield scrapy.Request(url, callback=self.parse_content)
        # i = 0;
        # for x in Datalist:
        #     Datalist[i] = "http://www.bagoum.com/cards/" + x.replace(" ","")
        #     yield scrapy.Request(Datalist[i], callback=self.parse_content)
        #     i += 1

        # for sel in response.xpath('//ul/li'):
        #     item = DmozItem()
        #     item['PicData'] = sel.xpath('//img/@src').extract()

        #     yield item
    def parse_content(self, response):

        print (response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract())
        # yield item

def createtable(cx,cu):
    cu.execute("create table image (name , role, src, type )")
    cx.commit()
def deletetable(cx,cu):
    cu.execute("drop table image")
    cx.commit()

