import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

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
    text_split = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
# Create a Document object 
    chunks = text_split.transform_documents([Document(page_content=extracted_data)])

    return chunks