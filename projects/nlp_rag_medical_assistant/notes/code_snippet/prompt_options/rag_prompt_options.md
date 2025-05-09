```
rag_prompt_template = """You are a medical assistant with expertise in healthcare.
    Use the following context from the Merck Manual to answer the question accurately.
    If the context doesn't contain the answer, say so and provide general medical knowledge.

    Context:
    {context}

    Question: {question}

    Answer:"""
```

```
def generate_response(self, question, context_chunks):
    prompt = f"""You are a helpful medical assistant with expertise in healthcare, trained on authoritative medical resources including the Merck Manuals.

    Please answer the following medical question accurately and comprehensively based on the provided reference information. Cite specific details from the reference material when possible.

    Reference Information:
    {context_chunks}

    Question: {question}

    Answer:"""

    return self.llm.invoke(prompt)
```