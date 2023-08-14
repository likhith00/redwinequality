from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger
from mlProject.pipeline.data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.model_trainer import ModelTrainerTrainingPipeline

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
    

STAGE_NAME = "Data Validation Stage"


if __name__ =="__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation Stage"


if __name__ =="__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Training Stage"


if __name__ =="__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e