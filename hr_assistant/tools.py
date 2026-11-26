"""Step 5: wrap the retriever as a tool can call"""

from langchain.tools import tool 


def create_search_tool(retriever):
    """
    Returns a tool that can be used to search for information the HE policy document
    """

    @tool
    def search_hr_policy(question: str) -> str:
        """
        Search the HR policy document for information about leave, work from home, probation, notice period, reimbursement, code of conduct, and other HR policies. Returns the relevant information as a string.
        """
        matching_chunks = retriever.invoke(question)
        return "\n\n".join([chunk.page_content for chunk in matching_chunks])
    
    return search_hr_policy