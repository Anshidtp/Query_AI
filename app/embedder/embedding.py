from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, texts: list) -> list:
        """
        Generate embeddings for a list of texts.
        """
        embeddings = self.model.encode(texts)
        return embeddings.tolist()