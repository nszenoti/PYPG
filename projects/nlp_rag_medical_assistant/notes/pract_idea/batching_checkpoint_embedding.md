

```python:batch_embedding.py
def batch_embed_documents(texts, embeddings_model, batch_size=20, checkpoint_file="embedding_checkpoint.pkl"):
    """Process document embeddings in batches with checkpointing."""
    import pickle
    import os

    embeddings = []
    start_idx = 0

    # Check if checkpoint exists
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'rb') as f:
            checkpoint_data = pickle.load(f)
            embeddings = checkpoint_data['embeddings']
            start_idx = checkpoint_data['next_idx']
            print(f"Resuming from checkpoint at index {start_idx}/{len(texts)}")

    try:
        # Process in batches with progress bar
        for i in tqdm(range(start_idx, len(texts), batch_size)):
            # Get the batch of texts
            batch = texts[i:i + batch_size]

            # Generate embeddings for the batch
            batch_embeddings = embeddings_model.embed_documents(batch)

            # Add to our list of embeddings
            embeddings.extend(batch_embeddings)

            # Save checkpoint after each batch
            checkpoint_data = {
                'embeddings': embeddings,
                'next_idx': i + batch_size
            }
            with open(checkpoint_file, 'wb') as f:
                pickle.dump(checkpoint_data, f)

    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Progress saved at index {start_idx + len(embeddings)}")
        # Checkpoint is already saved in the loop

    return embeddings
```

This implementation adds checkpointing to make the process robust:

1. Saves progress after each batch
2. Can resume from the last successful batch if interrupted
3. Maintains a checkpoint file with current embeddings and next index
4. Handles exceptions gracefully while preserving progress

When restarting, it will automatically pick up where it left off.
