from mlProject.pipeline.stage1_data_ingestion import DataIngestionPipeline 
from mlProject.pipeline.stage2_data_validation import DataValidationPipeline
from mlProject.pipeline.stage3_data_transfomation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage4_data_modelling import DataModellingPipeline
from mlProject.pipeline.stage5_data_evaluation import DataEvaluationPipeline
from mlProject import logger 


STAGE_NAME= "Data Ingestion Stage"
try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)



STAGE_NAME= "Data Validation Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)


STAGE_NAME= "Data Transformation Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME= "Data Modelling Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataModellingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)



STAGE_NAME= "Data Evaluation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)