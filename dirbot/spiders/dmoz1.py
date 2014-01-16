from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(BaseSpider):
    name = "test"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://en.wikipedia.org/wiki/Love"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.select('a/text()').extract()
            item['url'] = site.select('a/@href').extract()
            item['description'] = site.select('text()').re('-\s([^\n]*?)\\n')
            items.append(item)

        return items
