import streamlit as st
from langchain.embeddings import HuggingFaceEmbeddings  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Predefined documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership",
    "MS Dhoni is a former Indian Captain famous for his calm demeanor and finishing skill",
    "Sachin Tendulkar, also known as the 'God of cricket', holds many batting records",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers"
]

# Load embedding model once
@st.cache_resource
def load_embeddings_model():
    return HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

embedding = load_embeddings_model()

# Streamlit UI
st.title("Semantic Document Search")
st.write("Search through cricket players' descriptions using natural language!")

# Query input
query = st.text_input("Enter your query", value="who is bowler")

if query:
    # Get embeddings
    documents_embedding = embedding.embed_documents(documents)
    query_embedding = embedding.embed_query(query)

    # Compute cosine similarity
    similarities = cosine_similarity([query_embedding], documents_embedding)[0]
    index = int(np.argmax(similarities))
    score = similarities[index]

    # Output
    st.subheader("Top Matching Document:")
    st.write(f"**Query:** {query}")
    st.write(f"**Matched Document:** {documents[index]}")
    st.write(f"**Similarity Score:** {score:.4f}")
