from __future__ import annotations

import logging
import os

from helpers.data_source_fixture import DataSourceFixture

logger = logging.getLogger(__name__)


class SparkDataSourceFixture(DataSourceFixture):
    def __init__(self, test_data_source: str):
        super().__init__(test_data_source)

    def _build_configuration_dict(self, schema_name: str | None = None) -> dict:
        return {
            "data_source spark": {
                "type": "spark",
                "host": os.getenv("DATABRICKS_HOST"),
                "method": os.getenv("SPARK_METHOD"),
                "http_path": os.getenv("DATABRICKS_HTTP_PATH"),
                "token": os.getenv("DATABRICKS_TOKEN"),
                "catalog": os.getenv("DATABRICKS_CATALOG")
            }
        }

    def _create_schema_if_not_exists_sql(self) -> str:
        if os.getenv("SPARK_METHOD") == "databricks":
            logger.warning("Creating schema is not supported in databricks")
        else:
            logger.warning("TODO: Add create schema for odbc/hive local spark testing")
        return "SELECT 1"

    def _use_schema_sql(self) -> str | None:
        return None

    def _drop_schema_if_exists_sql(self):
        if os.getenv("SPARK_METHOD") == "databricks":
            logger.warning("Dropping schema is not supported in databricks")
        else:
            logger.warning("TODO: Add drop schema for odbc/hive local spark testing")
        return "SELECT 1"
