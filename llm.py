from langchain_google_genai import ChatGoogleGenerativeAI

def create_llm():
    """
    Create a Gemini language model.
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )
    return llm