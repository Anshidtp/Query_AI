from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag.retriever import retrieve_relevant_chunks
from app.rag.generator import generate_response
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

class Query(BaseModel):
    text: str

@router.post("/query_ai")
async def process_query(query: Query):
    try:
        relevant_chunks = retrieve_relevant_chunks(query.text)
        response = generate_response(query.text, relevant_chunks)
        logger.info(f"Response: {response}")
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))