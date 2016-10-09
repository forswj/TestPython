# -*- coding: utf-8 -*-

import scrapy


class AiriPicItem(scrapy.Item):

    airi_image_url=scrapy.Field()
    images=scrapy.Field()