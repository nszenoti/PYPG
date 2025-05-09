def extract_embeddings_from_faiss(vector_store_path="merck_manual_faiss_index"):
    """
    Extract embeddings, texts, and metadata from a saved FAISS vector store.

    Args:
        vector_store_path (str): Path to the saved FAISS vector store

    Returns:
        tuple: (texts, embeddings, metadatas) or (None, None, None) if extraction fails
    """
    import pickle
    import numpy as np
    from langchain_aws import BedrockEmbeddings
    from langchain_community.vectorstores import FAISS

    try:
        # Initialize embedding model (needed for loading)
        embeddings_model = BedrockEmbeddings(
            client=bedrock_client,
            model_id="amazon.titan-embed-text-v2:0",
            model_kwargs={"dimensions": 516}
        )

        # Load the vector store
        vector_store = FAISS.load_local(vector_store_path, embeddings_model)

        # Load the docstore data from the index.pkl file
        docstore_path = os.path.join(vector_store_path, "index.pkl")
        with open(docstore_path, "rb") as f:
            docstore_data = pickle.load(f)

        # Extract texts and metadata
        texts = []
        metadatas = []

        # The docstore contains the mapping between IDs and documents
        for doc_id, doc in docstore_data["docstore"]._dict.items():
            texts.append(doc.page_content)
            metadatas.append(doc.metadata)

        # Extract embeddings from the FAISS index
        # This gets the raw numpy array of all embeddings
        embeddings = vector_store.index.reconstruct_n(0, vector_store.index.ntotal)

        print(f"Extracted {len(texts)} texts, {len(embeddings)} embeddings, and {len(metadatas)} metadata entries")

        # Convert numpy arrays to lists for easier serialization
        embeddings_list = [emb.tolist() for emb in embeddings]

        return texts, embeddings_list, metadatas

    except Exception as e:
        print(f"Error extracting data from FAISS index: {e}")
        return None, None, None

# Usage
# texts, embeddings, metadatas = extract_embeddings_from_faiss()
# if embeddings is not None:
#     # Save as backup
#     save_embeddings_backup(texts, embeddings, metadatas)