from src.simple_mlops.config.configuration import ConfigurationManager
from src.simple_mlops.components.model_trainer import ModelTrainer
from src.simple_mlops import logger


STAGE_NAME = "Model Trainer Stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def run_training_pipeline(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


# if __name__ == "__main__":
#     try:
#         logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
#         obj = ModelTrainerTrainingPipeline()
#         obj.run_training_pipeline()
#         logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
#     except Exception as e:
#         logger.exception(e)
#         raise e