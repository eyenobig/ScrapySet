import scrapy
# import json
import time
import requests
from icchi.items import CharacterItem

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

        for x in listurl:
            # wikiru采用0.3秒不能连开同网页 做了一点傻瓜调整
            yield scrapy.Request(x,callback=self.parse_content)
            time.sleep(0.4)


        #         yield scrapy.Request(x,callback=self.parse_content)
            # yield scrapy.Request(x,callback=self.parse_content)
        #
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
        item = CharacterItem()
        name = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
        if name:
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
            # item['rarity'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[3]/td/text()').extract()
            # item['generation'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[4]/td/text()').extract()
            # item['race'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[5]/td/text()').extract()
            # item['arms'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[6]/td/text()').extract()
            # item['FavoriteGift'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[7]/td/text()').extract()
            # item['MaterialCost'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[8]/td/text()').extract()
            # item['ExpGroup'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[9]/td/text()').extract()
            # item['Engraved'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[10]/td/text()').extract()
            heroSmriti = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[12]/td/a/text()').extract()
            item['heroSmriti']  = str(heroSmriti)
            # item['heroSmriti'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[12]/td/a/text()').extract()
            # item['detail'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[14]/td/text()').extract()
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
            # item['name'] = response.xpath('//*[@id="body"]/div[2]/table/tbody/tr[2]/td[2]/text()').extract()
        else:
            item['name'] = 'Data'
        yield item

def createtable(cx,cu):
    cu.execute("create table image (name , role, src, type )")
    cx.commit()
def deletetable(cx,cu):
    cu.execute("drop table image")
    cx.commit()

