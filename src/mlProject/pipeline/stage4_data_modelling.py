from mlProject.components.data_modelling import ModelTrainer
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger


STAGE_NAME= "Data Modelling Stage"

class DataModellingPipeline:
    def __init__(self) -> None:
        pass
        
        
    def main(self):
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
       
       


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataModellingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
