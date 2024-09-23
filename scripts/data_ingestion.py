from tqdm import tqdm
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.data.loader import load_data
from app.data.preprocessor import preprocess_text, segment_text
from app.embedder.embedding import generate_embedding
from app.database.vectordb import upsert_to_pinecone
# from app.config import PINECONE_API_KEY, PINECONE_ENVIRONMENT, PINECONE_INDEX_NAME

import pinecone

# def load_data(file_path):
#     return pd.read_csv(file_path)

def process_and_store_data(file_path):
    # # Initialize Pinecone
    # pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
    
    # # Create index if it doesn't exist
    # if PINECONE_INDEX_NAME not in pinecone.list_indexes():
    #     pinecone.create_index(PINECONE_INDEX_NAME, dimension=384, metric="cosine")
    
    # Load data
    df = load_data(file_path)
    
    
    # Process each resume
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing resumes"):
        # Combine relevant fields into a single text
        text = row['Resume_str']
        
        # Preprocess the text
        preprocessed_text = preprocess_text(text)
        
        # Segment the text
        segments = segment_text(preprocessed_text)
        
        # Generate embeddings and store in Pinecone
        for i, segment in enumerate(segments):
            embedding = generate_embedding(segment.page_content)
            metadata = {
                "id": f"{index}_{i}",
                "text": segment,
                "original_index": index
            }
            upsert_to_pinecone([embedding], [metadata])
    
    print("Data ingestion completed successfully!")

if __name__ == "__main__":
    data_file_path = "dataset/Resume.csv"
    process_and_store_data(data_file_path)