from src.simple_mlops import logger
from src.simple_mlops.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.simple_mlops.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.simple_mlops.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.simple_mlops.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline 


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

    STAGE_NAME = "Data Transformation Stage"
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.run_transformation_pipeline()      # <- note: different method name
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Model Trainer Stage"
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.run_training_pipeline()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e