from mlProject.components.data_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger


STAGE_NAME= "Data Evaluation Stage"

class DataEvaluationPipeline:
    def __init__(self) -> None:
        pass
        
        
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
       
       


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)



