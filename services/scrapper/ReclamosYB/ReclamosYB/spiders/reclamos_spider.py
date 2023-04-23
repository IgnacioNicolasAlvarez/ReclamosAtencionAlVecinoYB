import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ReclamosYB.config import settings
from ReclamosYB.items import ReclamosybItem


class ReclamosSpider(CrawlSpider):
    name = "reclamos"

    years = ["2023", "2022"]
    meses = {
        "enero": "01",
        "febrero": "02",
        "marzo": "03",
        "abril": "04",
        "mayo": "05",
        "junio": "06",
        "julio": "07",
        "agosto": "08",
        "septiembre": "09",
        "octubre": "10",
        "noviembre": "11",
        "diciembre": "12",
    }

    allowed_domains = [settings.ALLOWED_DOMAIN]
    default_url = settings.DEFAULT_URL
    start_urls = [
        settings.START_URL,
    ]

    rules = (
        Rule(
            LinkExtractor(restrict_css=".pagination a"),
            callback="parse",
            follow=True,
        ),
    )

    def parse(self, response, **kwargs):
        for r in response.css("li.dataset-item"):
            title = r.css("h2 a::text").get()
            link = self.default_url + r.css("h2 a::attr(href)").get()

            match = re.search(r"(\w+)-(\d{4})", link)
            anio = match.group(2)

            if anio in self.years:
                mes = match.group(1)
                if mes.lower() in self.meses:
                    mes = self.meses[mes.lower()]

                item = {"title": title, "mes": mes, "anio": anio}
                yield scrapy.Request(link, callback=self.parse_item, meta=item)

    def parse_item(self, response):
        for r in response.css("li.resource-item"):
            resource_name = r.css("a::text").get().strip()
            _href_link = r.css("a::attr(href)").get().strip()

            rl = self.default_url + _href_link
            item = {
                "title": response.meta["title"],
                "resource_name": resource_name,
                "mes": response.meta["mes"],
                "anio": response.meta["anio"],
            }
            yield scrapy.Request(rl, callback=self.parse_subitem, meta=item)

    def parse_subitem(self, response):
        __css_mask = "a.resource-url-analytics::attr(href)"
        resource_link = response.css(__css_mask).get()
        item = ReclamosybItem(
            {
                "title": response.meta["title"],
                "mes": response.meta["mes"],
                "anio": response.meta["anio"],
                "resource_name": response.meta["resource_name"],
                "resource_link": resource_link,
            }
        )

        yield item
