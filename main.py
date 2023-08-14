from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger
from mlProject.pipeline.data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


if __name__ =="__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e