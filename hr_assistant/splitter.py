"""Step 2: chop the documents into small searchable chunks."""


from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config


def split_into_chunks(documents):
    """
        Split documents into small overlapping chunks for better searchability.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
    )
    chunks = text_splitter.split_documents(documents)

    return chunks
