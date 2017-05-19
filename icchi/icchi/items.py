# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IcchiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CharacterItem(scrapy.Item):
    name = scrapy.Field()
    rarity = scrapy.Field()
    generation = scrapy.Field()
    race = scrapy.Field()
    arms = scrapy.Field()
    FavoriteGift = scrapy.Field()
    MaterialCost = scrapy.Field()
    ExpGroup = scrapy.Field()
    Engraved = scrapy.Field()
    heroSmriti = scrapy.Field()
    detail = scrapy.Field()
    Esoteric = scrapy.Field()
    overt_rankUP = scrapy.Field()
    shade_rankUP = scrapy.Field()

