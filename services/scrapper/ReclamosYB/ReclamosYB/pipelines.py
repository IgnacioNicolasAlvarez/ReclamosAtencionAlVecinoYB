from scrapy.exceptions import DropItem

from ReclamosYB.logger import logger


class ReclamosybPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        if item["resource_link"] is not None:
            item["resource_name"] = item["resource_name"].split(".")[0]
            return item
        else:
            logger.warning("Missing resource_link in %s", item)
            raise DropItem("Missing resource_link in %s" % item)
