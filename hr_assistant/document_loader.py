"""Step 1: Load documents from a directory and split them into chunks."""


from langchain_community.document_loaders import TextLoader
from hr_assistant import config


def load_document(file_path: str = config.DATA_PATH):
    """
    Load a document from the specified file path and return it as a list of documents.

    Args:
        file_path (str): The path to the document file.
    """

    # Load the document using TextLoader
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    return documents