from langchain_aws import BedrockEmbeddings

# Initialize the Titan Embeddings v2 model with 516 dimensions
embeddings = BedrockEmbeddings(
    client=bedrock_client,
    model_id="amazon.titan-embed-text-v2:0",
    model_kwargs={"dimensions": 516}  # Specify 516 dimensions
)