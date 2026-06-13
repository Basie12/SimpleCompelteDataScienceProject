from src.simple_mlops.config.configuration import ConfigurationManager
from src.simple_mlops.components.data_transformation import DataTransformation
from src.simple_mlops import logger


STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def run_transformation_pipeline(self):
        try:
            config = ConfigurationManager()

            # pull the status file path from config instead of hardcoding it
            status_file = config.get_data_validation_config().STATUS_FILE

            with open(status_file, "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid")

        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.run_transformation_pipeline()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e