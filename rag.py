from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


def create_rag_chain(retriever, llm):
    """
    Create a Retrieval-Augmented Generation (RAG) chain.
    """
    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful and creative AI assistant.

        Answer the user's question using the provided context whenever possible.

        If the answer is fully supported by the context:
        - Clearly state the answer.

        If the context is incomplete:
        - You may use your own knowledge or make a reasonable inference.
        - Clearly indicate that this part is an inference or a guess.
        - Do not present guesses as facts.

        Context:
        {context}

        Question:
        {input}
        """
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    rag_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return rag_chain