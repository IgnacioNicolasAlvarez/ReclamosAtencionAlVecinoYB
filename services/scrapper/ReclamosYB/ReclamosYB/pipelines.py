import pandas as pd
import polars as pl
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ReclamosybPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        if item["resource_link"] is not None:
            return item
        else:
            raise DropItem("Missing resource_link in %s" % item)
