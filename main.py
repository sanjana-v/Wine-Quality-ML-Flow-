from mlProject.pipeline.stage1_data_ingestion import DataIngestionPipeline
from mlProject import logger 


STAGE_NAME= "Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)