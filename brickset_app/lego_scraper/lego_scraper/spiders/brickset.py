# -*- coding: utf-8 -*-
import scrapy


class BricksetSpider(scrapy.Spider):
    name = 'brickset'
    allowed_domains = ['brickset.com']
    start_urls = ['http://brickset.com/sets/year-2017/']

    def parse(self, response):
        for brickset in response.css('article.set'):
            meta = brickset.css('div.meta')
            # セット番号を取得
            number = meta.css('h1 a span::text').re_first(r'\d+')

            # セット名を取得
            name = brickset.css('div.highslide-caption h1::text').extract_first()
            print(number, name)
            yield {
                'number': number,
                'name': name,
                'image': brickset.css('img::attr(src)').re_first('(.*)\?'),
                'theme': meta.css('.tags a')[1].css('a::text').extract_first(),
                'subtheme': meta.css('.tags a.subtheme::text').extract_first(),
                'year': meta.css('.rating::attr(title)').extract_first(),
                'owner': brickset.css('dl.admin dd').re_first('(\d+) own this set'),
                'want_it': brickset.css('dl.admin dd').re_first('(\d+) want it')
            }
            next_url = response.css('li.next a::attr("href")').extract_first()
            if next_url:
                yield scrapy.Request(next_url)
