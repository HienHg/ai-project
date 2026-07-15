from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into smaller overlapping chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)
    return chunks