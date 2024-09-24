# Query_AI

This is a Retrieval-Augmented Generation (RAG) system that processes unstructured data, generates embeddings, stores them in a vector database, and uses them to answer queries.

![Demo](https://github.com/Anshidtp/Query_AI/blob/main/example/Frontend.png)


## Requirements:
 * Python 3.8+ or later
 * FastAPI
 * LangChain
 * Llama-3
 * GROQ
 * Pinecone
 * HTML, CSS, JavaScript (for the frontend)


## Steps To Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create and activate a virtual environment:**

    ```bash
    conda activate -n <env_name> python=3.11 -y
    conda activate <env_name>
    ```
    Repalce the <env_name> with the name of your environment 

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add your Replicate API token

    ```env
    #REPLICATE
    REPLICATE_API_TOKEN=your_replicate_api_token

    PINECONE_API_KEY = "Your_PINECONE_API_KEY"
    PINECONE_Region = "Your_PINECONE_Region"
    PINECONE_INDEX_NAME = "Your_PINECONE_INDEX_NAME"
    Groq_API_KEY = "Your_Groq_API_KEY"

    ```

5. **Running the Application:**
    Launch your terminal and execute the following command:

   1.  Run the Data Ingestion Pipeline

        ```bash
        python scripts/data_ingestion.py
        ```
   2. Run the Application
        ```bash
        python run.py
        ```
