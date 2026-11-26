"""Step 3: turn text into numbers(vectors) using Jina"""


from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config


def get_embeddings_model():
    """
        Get the Jina embeddings model for converting text into vector representations.
        Read JINA_API_KEY from environment variables.
    """
    embeddings_model = JinaEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        # model_kwargs={"device": config.EMBEDDINGS_MODEL_DEVICE},
    )

    return embeddings_model