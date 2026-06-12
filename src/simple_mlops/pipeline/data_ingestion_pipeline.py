from src.simple_mlops.components.data_ingestion import DataIngestion
from src.simple_mlops.config.configuration import ConfigurationManager
from src.simple_mlops import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()
    
# if __name__ == "__main__":
#     try:
#         logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
#         data_ingestion_pipeline = DataIngestionTrainingPipeline()
#         data_ingestion_pipeline.run_pipeline()
#         logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
#     except Exception as e:
#         logger.exception(e)
#         raise e