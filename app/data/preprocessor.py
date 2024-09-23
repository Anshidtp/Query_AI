import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from langchain.text_splitter import RecursiveCharacterTextSplitter

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text: str) -> str:
    """
    Clean and preprocess the input text.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Join tokens back into a string
    cleaned_text = " ".join(tokens)
    
    return cleaned_text

# def segment_text(text: str, chunk_size: int = 100) -> list:
#     """
#     Segment the text into chunks based on word count.
#     """
#     words = text.split()
#     chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
#     return chunks

# Create text chunks for extracted data
def segment_text(extracted_data):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500 , chunk_overlap = 40)
    chunks = splitter.split_documents(extracted_data)

    return chunks