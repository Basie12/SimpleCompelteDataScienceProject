from src.simple_mlops import logger
from src.simple_mlops.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.simple_mlops.pipeline.data_validation_pipeline import DataValidationTrainingPipeline


if __name__ == "__main__":

    STAGE_NAME = "Data Ingestion Stage"
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.run_pipeline()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e

    STAGE_NAME = "Data Validation Stage"
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.run_pipeline()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e