from cnnClassifier.config.configuration import (ConfigurationManager)
from cnnClassifier.components.model_evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Model Evaluation"


class ModelEvaluationPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"******************************************")
        logger.info(f"Starting {STAGE_NAME}.....................")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed successfully!")
    except Exception as e:
        logger.exception(e)
        raise e