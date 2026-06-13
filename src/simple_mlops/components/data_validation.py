import os
from src.simple_mlops import logger
import pandas as pd
from src.simple_mlops.entity.config_entity import DataValidationConfig
# from src.simple_mlops.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates that the dataset's columns and dtypes match the schema.
        Writes the result to STATUS_FILE and returns the status.
        """
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir, sep=";")  # semicolon-delimited
            all_cols = list(data.columns)
            schema_cols = self.config.all_schema.keys()

            # 1) every column in the data must be declared in the schema
            for col in all_cols:
                if col not in schema_cols:
                    validation_status = False
                    logger.info(f"Unexpected column not in schema: {col}")

            # 2) every column in the schema must be present in the data
            for col in schema_cols:
                if col not in all_cols:
                    validation_status = False
                    logger.info(f"Missing expected column: {col}")

            # 3) dtypes must match the schema
            for col, expected_dtype in self.config.all_schema.items():
                if col in data.columns:
                    actual_dtype = str(data[col].dtype)
                    if actual_dtype != expected_dtype:
                        validation_status = False
                        logger.info(
                            f"Dtype mismatch in '{col}': "
                            f"expected {expected_dtype}, got {actual_dtype}"
                        )

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            logger.info(f"Validation status: {validation_status}")
            return validation_status

        except Exception as e:
            raise e
