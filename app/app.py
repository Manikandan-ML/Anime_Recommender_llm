import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title = "Anime Recommender",layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender system")

query = st.text_input("enter your anime preferences eg: light hearted anime with school setting")

if query:
    with st.spinner("Fetching recommendation for you..."):
        response = pipeline.recommend(query)
        st.markdown('### Recommendations')
        st.write(response)