"""Step 6: connect to the LLM(the "brain" of the assistant)"""


from langchain_groq import ChatGroq
from hr_assistant import config


def get_llm():
    """
    Returns a ChatGroq instance that can be used to generate responses to user queries.
    """
    return ChatGroq(
        model=config.LLM_MODEL_NAME,
        api_key=config.GROQ_API_KEY,
        temperature=0.2,
        max_tokens=512,
    )