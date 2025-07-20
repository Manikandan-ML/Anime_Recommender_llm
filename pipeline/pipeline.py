from src.vector_store import Vector_store_builder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Initialzing Recommendation Pipeline")

            vector_builder = Vector_store_builder(csv_path="",persist_dir = persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipeline Initiated successfully...")
        
        except Exception as e:
            import traceback
            logger.error(f"Pipeline initialization error: {traceback.format_exc()}")
            #logger.error(f"Failed to initialize pipeline{str(e)}")
            raise CustomException("Error during pipeline intialization",e)
    
    def recommend(self,query:str):
        try:
            logger.info(f"Recieved a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucessfully")
            return recommendation
        except Exception as e:
            logger.error(f"failed to get recommedation {str(e)}")
            raise CustomException("Error during getting  recommendation",e)
        
            