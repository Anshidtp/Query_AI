from app.embedder.embedding import Embedder
from app.database.vectordb import query_pinecone

embedder = Embedder()
#vector_db = VectorDB()

def retrieve_relevant_chunks(query: str, top_k: int = 5) -> list:
    """
    Retrieve the most relevant chunks for a given query.
    """
    query_embedding = embedder.generate_embeddings([query])[0]
    results = query_pinecone(query_embedding, top_k=top_k)
    relevant_chunks = [result['metadata']['text'] for result in results['matches']]
    return relevant_chunks