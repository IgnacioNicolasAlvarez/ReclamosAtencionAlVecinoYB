from scrapy.exceptions import DropItem

from ReclamosYB.logger import logger
import pandas as pd


class ReclamosybPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        if item["resource_link"] is not None:
            item["resource_name"] = item["resource_name"].split(".")[0]
            self._save_to_gbq(item)
            return item
        else:
            logger.warning("Missing resource_link in %s", item)
            raise DropItem("Missing resource_link in %s" % item)

    @staticmethod
    def _save_to_gbq(item):
        df = pd.read_excel(item["resource_link"])
        df.to_gbq(
            destination_table=".dataset_yb"
            + item["resource_name"]
            + item["mes"]
            + item["anio"],
            project_id="",
            progress_bar=True,
            if_exists="replace"
        )
