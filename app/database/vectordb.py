import pinecone
from app.config import settings
from typing import Dict, Any, List
from pinecone import Pinecone,ServerlessSpec
import time
from langchain.schema import Document

def connect_vecdb():
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)
    spec = ServerlessSpec(cloud="aws", region=settings.PINECONE_Region)

    index_name = settings.PINECONE_INDEX_NAME
    existing_indexes = [
        index_info["name"] for index_info in pc.list_indexes()
    ]

    # check if index already exists (it shouldn't if this is first time)
    if index_name not in existing_indexes:
        # if does not exist, create index
        pc.create_index(
            index_name,
            dimension=1536,  # dimensionality of ada 002
            metric='cosine',
            spec=spec
        )
        # wait for index to be initialized
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)

    # connect to index
    index = pc.Index(index_name)
    time.sleep(1)
    # view index stats
    index.describe_index_stats()
    return index


# class VectorDB:
#     def __init__(self):
#         pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT)
#         self.index_name = "resume-embeddings"
#         if self.index_name not in pinecone.list_indexes():
#             pinecone.create_index(self.index_name, dimension=384)  # Dimension for 'all-MiniLM-L6-v2'
#         self.index = pinecone.Index(self.index_name)

#     def upsert_vectors(self, vectors: list, metadata: list):
#         """
#         Upsert vectors and metadata into the Pinecone index.
#         """
#         to_upsert = list(zip(range(len(vectors)), vectors, metadata))
#         self.index.upsert(vectors=to_upsert)

#     def query(self, query_vector: list, top_k: int = 5):
#         """
#         Query the Pinecone index for similar vectors.
#         """
#         results = self.index.query(query_vector, top_k=top_k, include_metadata=True)
#         return results

#Upsert a vector and its metadata to Pinecone.
def upsert_to_pinecone(vectors: list, metadata: list):
    index = connect_vecdb()
    to_upsert = []
    for i, (vector, meta) in enumerate(zip(vectors, metadata)):
        # Ensure 'id' is present in the metadata, and 'text' is a string
        vector_id = meta.get('id', str(i))  # Fallback to 'i' if no 'id' is found
        
        # Convert 'text' field to string if it's not already
        if isinstance(meta.get('text'), Document):
            meta['text'] = str(meta['text'])  # Extract or convert to string
            
        # If other fields in meta are complex objects, convert them similarly
        
        to_upsert.append({
            "id": vector_id,         # The vector ID
            "values": vector,        # The embedding vector
            "metadata": meta         # The metadata, now properly formatted
        })
    
    # Perform the upsert operation
    index.upsert(vectors=to_upsert)

def query_pinecone(query_vector: List[float], top_k: int = 5) -> Dict[str, Any]:
    """
    Query Pinecone for the most similar vectors.

    Args:
        query_vector (List[float]): The query vector.
        top_k (int, optional): The number of results to return. Defaults to 5.
    Returns:
        Dict[str, Any]: The query results.
    """
    index = connect_vecdb()
    return index.query(vector=query_vector, top_k=top_k, include_metadata=True)