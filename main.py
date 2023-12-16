from mlProject.pipeline.stage1_data_ingestion import DataIngestionPipeline 
from mlProject.pipeline.stage2_data_validation import DataValidationPipeline
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
