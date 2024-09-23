import openai
from app.config import settings

openai.api_key = settings.Open_API_KEY

def generate_response(query: str, relevant_chunks: list) -> str:
    """
    Generate a response using the OpenAI API based on the query and relevant chunks.
    """
    context = "\n".join(relevant_chunks)
    prompt = f"Based on the following resume information:\n\n{context}\n\nAnswer the following question: {query}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on resume information."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content']