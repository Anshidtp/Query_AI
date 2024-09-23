from sentence_transformers import SentenceTransformer

# class Embedder:
#     def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
#         self.model = SentenceTransformer(model_name)

#     def generate_embeddings(self, texts: list) -> list:
#         """
#         Generate embeddings for a list of texts.
#         """
#         embeddings = self.model.encode(texts)
#         return embeddings.tolist()

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_embedding(text: str):
    """
    Generate an embedding for the input text.

    Args:
        text (str): The input text to generate an embedding for.

    Returns:
        List[float]: The generated embedding as a list of floats.
    """
    return model.encode(text).tolist()