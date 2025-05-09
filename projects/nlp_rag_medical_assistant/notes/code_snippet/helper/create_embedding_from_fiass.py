def extract_embeddings_from_faiss(index_path, embedding_model):
    """
    Extract all embeddings from a saved FAISS index.

    Args:
        index_path (str): Path to the saved FAISS index
        embedding_model: The embedding model used to create the index

    Returns:
        list: List of embedding vectors
        list: List of corresponding documents
    """
    from langchain.vectorstores import FAISS
    import numpy as np

    # Load the FAISS index
    vector_store = FAISS.load_local(index_path, embedding_model)

    # Get number of vectors in the index
    num_vectors = vector_store.index.ntotal

    # Extract all embeddings
    embeddings = [vector_store.index.reconstruct(i) for i in range(num_vectors)]

    # Get the corresponding documents
    documents = [vector_store.docstore.search(vector_store.index_to_docstore_id[i])
                for i in range(num_vectors)]

    return embeddings, documents