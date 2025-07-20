from src.data_loader import AnimeDataloader
from src.vector_store import Vector_store_builder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipelines")

        loader = AnimeDataloader("data/anime_with_synopsis.csv","data/anime_updated.csv")

        processed_csv = loader.load_and_process()

        logger.info("Data loaded and Processed..")

        vector_builder = Vector_store_builder(processed_csv)
        vector_builder.build_and_save_vector_store()

        logger.info("Vector store Build sucesfully...")

        logger.info("Pipeline build sucessfully")
    
    except Exception as e:
        logger.error(f"failed to execute pipeline {str(e)}")
        raise CustomException("Error during pipeline execution",e)
    
if __name__ =="__main__":
    main()



