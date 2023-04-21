from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import polars as pl
import pandas as pd


class ReclamosybPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        if item["resource_link"] is not None:
            df = pd.read_excel(item["resource_link"])
            df.write_csv(f"./output/data.csv")
            return item
        else:
            raise DropItem("Missing resource_link in %s" % item)
