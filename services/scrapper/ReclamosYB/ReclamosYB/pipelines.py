import numpy as np
import pandas as pd
from scrapy.exceptions import DropItem

from ReclamosYB.config import settings
from ReclamosYB.logger import logger


def replace_nulls(col):
    if col.dtype == "object":
        return col.fillna("DEFAULT")
    elif np.issubdtype(col.dtype, np.number):
        return col.fillna(col.mean())
    else:
        return col


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
        df.columns = df.columns.str.replace(" ", "_")
        df.columns = df.columns.str.replace("ñ", "ni")

        df["anio"] = item["anio"]
        df["mes"] = item["mes"]

        df = df.apply(replace_nulls)

        df.to_gbq(
            destination_table=f"{settings.PROJECT_ID}.dataset_yb."
            + item["resource_name"],
            project_id=settings.PROJECT_ID,
            progress_bar=True,
            chunksize=None,
            if_exists="append",
        )
