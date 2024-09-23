from pydantic_settings import BaseSettings

from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    PINECONE_API_KEY: str
    PINECONE_Region: str
    PINECONE_INDEX_NAME: str
    Open_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()