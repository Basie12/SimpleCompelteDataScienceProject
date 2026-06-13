from src.simple_mlops.config.configuration import ConfigurationManager
from src.simple_mlops.components.model_evaluation import ModelEvaluation 
from src.simple_mlops import logger
STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def run_evaluation_pipeline(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()