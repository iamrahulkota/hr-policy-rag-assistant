import os
from dotenv import load_dotenv



load_dotenv()

# Load environment variables from .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")


# Define path - data, vectorstore paths
DATA_PATH = os.path.join("data", "hr_policy.txt")
VECTOR_STORE_PATH = os.path.join("data", "faiss_index")

# Define models
LLM_MODEL_NAME = "openai/gpt-oss-120b"
EMBEDDING_MODEL_NAME = "jina-embeddings-v5-text-small"

# Chunk / text splitting parameters
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrieval parameters
TOP_K_RESULTS = 3

# System prompt
SYSTEM_PROMPT = """
    You are a friendly HR assistant.
    Always use the search_hr_policy tool to look up
    facts before answering.
    If the answer isn't in the search results, say you don't know instead of guessing.
"""


def check_api_keys():
    """
    Check if the required API keys are set in the environment variables.
    If not, raise an exception with a message indicating which keys are missing.
    """
    missing_keys = []
    if not GROQ_API_KEY:
        missing_keys.append("GROQ_API_KEY")
    if not JINA_API_KEY:
        missing_keys.append("JINA_API_KEY")

    if missing_keys:
        raise EnvironmentError(
            f"Missing required API keys: {', '.join(missing_keys)}. "
            "Please set them in your environment variables or .env file."
        )
    