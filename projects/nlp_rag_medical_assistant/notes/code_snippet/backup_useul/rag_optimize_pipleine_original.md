```
def optimize_rag_pipeline(chunks, question):
    """Test different RAG configurations for a question."""

    # Configuration variations to test
    configurations = [
        # Variation 1: Default configuration
        {
            "chunk_size": 1000,
            "chunk_overlap": 200,
            "retriever_k": 5,
            "llm_params": {"temperature": 0.5, "maxTokenCount": 1500}
        },
        # Variation 2: Smaller chunks, more retrieval
        {
            "chunk_size": 500,
            "chunk_overlap": 100,
            "retriever_k": 8,
            "llm_params": {"temperature": 0.4, "maxTokenCount": 1500}
        },
        # Variation 3: Larger chunks, less retrieval
        {
            "chunk_size": 1500,
            "chunk_overlap": 300,
            "retriever_k": 3,
            "llm_params": {"temperature": 0.5, "maxTokenCount": 1800}
        },
        # Variation 4: More creative generation
        {
            "chunk_size": 1000,
            "chunk_overlap": 200,
            "retriever_k": 5,
            "llm_params": {"temperature": 0.7, "maxTokenCount": 1500}
        },
        # Variation 5: More precise generation
        {
            "chunk_size": 1000,
            "chunk_overlap": 200,
            "retriever_k": 5,
            "llm_params": {"temperature": 0.2, "maxTokenCount": 1500}
        }
    ]


    print(f"Testing RAG configurations for question: {question} --->")

    results = []
    for i, config in enumerate(configurations):
        print(f"Testing RAG configuration {i+1}...")

        # Re-split text if chunk size is different
        if config["chunk_size"] != 1000 or config["chunk_overlap"] != 200:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=config["chunk_size"],
                chunk_overlap=config["chunk_overlap"],
                separators=["\n\n", "\n", ". ", " ", ""],
                length_function=len
            )
            test_chunks = text_splitter.create_documents([raw_text])
            for j, chunk in enumerate(test_chunks):
                chunk.metadata = {"chunk_id": j, "source": "Merck Manual"}

            # Create new vector store
            test_vector_store = create_vector_store(test_chunks)
        else:
            test_vector_store = vector_store

        # Create retriever with specific k value
        test_retriever = test_vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": config["retriever_k"]}
        )

        # Initialize LLM with specific parameters
        test_llm = initialize_llm_for_rag(**config["llm_params"])

        # Create RAG prompt
        rag_prompt_template = """You are a medical assistant with expertise in healthcare.
        Use the following context from the Merck Manual to answer the question accurately.
        If the context doesn't contain the answer, say so and provide general medical knowledge.

        Context:
        {context}

        Question: {question}

        Answer:"""

        rag_prompt = PromptTemplate.from_template(rag_prompt_template)

        # Create RAG chain
        test_rag_chain = (
            {"context": test_retriever, "question": RunnablePassthrough()}
            | rag_prompt
            | test_llm
            | StrOutputParser()
        )

        # Generate response
        response = test_rag_chain.invoke(question)

        results.append({
            "configuration": i+1,
            "settings": config,
            "response": response
        })

    return results
```