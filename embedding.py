from langchain_google_genai import GoogleGenerativeAIEmbeddings

def create_embeddings():
    """
    Create a Google Generative AI embedding model.
    """
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )
    return embeddings