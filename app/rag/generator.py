
from app.config import settings
from langchain_pinecone import PineconeVectorStore
from ..database.vectordb import connect_vecdb
from ..embedder.embedding import model
from groq import Groq
client = Groq(
    api_key=settings.Groq_API_KEY,
    
)

vector_store = PineconeVectorStore(index=connect_vecdb(), embedding=model)




def generate_response(query: str, relevant_chunks: list) -> str:
    """
    Generate a response using the OpenAI API based on the query and relevant chunks.
    """
    context = "\n".join(relevant_chunks)
    prompt = f"Based on the following  information:\n\n{context}\n\nAnswer the following question: {query}"

    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": """You are a helpful assistant that answers questions based on the information.
                                            if you dont't know the answer, just say i don't have knowledge about it, don't try to make up an answer,
                                            Remember to keep your responses concise and Only return the helpful answer below and nothing else.
                                            Answer :"""},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content