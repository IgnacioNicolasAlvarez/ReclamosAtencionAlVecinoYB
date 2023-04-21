import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ReclamosYB.items import ReclamosybItem


class ReclamosSpider(CrawlSpider):
    name = "reclamos"
    allowed_domains = ["datos.yerbabuena.gob.ar"]
    default_url = "http://datos.yerbabuena.gob.ar"
    start_urls = [
        "http://datos.yerbabuena.gob.ar/organization/atencion-al-vecino?page=1",
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
            item = {"title": title}
            yield scrapy.Request(link, callback=self.parse_item, meta=item)

    def parse_item(self, response):
        for r in response.css("li.resource-item"):
            resource_name = r.css("a::text").get().strip()
            resource_link = self.default_url + r.css("a::attr(href)").get().strip()
            item = {"title": response.meta["title"], "resource_name": resource_name}
            yield scrapy.Request(resource_link, callback=self.parse_subitem, meta=item)

    def parse_subitem(self, response):
        resource_link = response.css("a.resource-url-analytics::attr(href)").get()
        item = ReclamosybItem(
            {
                "title": response.meta["title"],
                "resource_name": response.meta["resource_name"],
                "resource_link": resource_link,
            }
        )
        yield item
