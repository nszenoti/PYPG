from tqdm.notebook import tqdm

def batch_embed_documents(texts, embeddings_model, batch_size=20):
    """Process document embeddings in batches."""
    embeddings = []

    # Process in batches with progress bar
    for i in tqdm(range(0, len(texts), batch_size)):
        # Get the batch of texts
        batch = texts[i:i + batch_size]

        # Generate embeddings for the batch
        batch_embeddings = embeddings_model.embed_documents(batch)

        # Add to our list of embeddings
        embeddings.extend(batch_embeddings)

    return embeddings

# When creating vector store
chunks = split_text(raw_text)
texts = [chunk.page_content for chunk in chunks]
metadatas = [chunk.metadata for chunk in chunks]

# Generate embeddings in batches
embeddings_model = BedrockEmbeddings(
    client=bedrock_client,
    model_id="amazon.titan-embed-text-v2:0",
    model_kwargs={"dimensions": 516}
)

# Get embeddings with batching
document_embeddings = batch_embed_documents(texts, embeddings_model, batch_size=20)

# Create vector store from embeddings
vector_store = FAISS.from_embeddings(
    text_embeddings=list(zip(texts, document_embeddings)),
    embedding=embeddings_model,
    metadatas=metadatas
)