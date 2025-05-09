Yes, exactly — if you do:

```python
vector_store.save_local("faiss_index")
```

Then the `faiss_index/` folder is created **in the current working directory** — i.e., the same folder where your notebook or script is running, unless you specify a different path.

---

### ✅ To confirm or control the path:

You can check or print the current working directory like this:

```python
import os
print(os.getcwd())
```

Or specify a full path manually:

```python
vector_store.save_local("/home/ec2-user/my_rag_project/faiss_index")
```

Then load with the same path:

```python
vector_store = FAISS.load_local("/home/ec2-user/my_rag_project/faiss_index", embeddings=embeddings)
```

---

Do you plan to persist it elsewhere (like S3 or EBS) or just keep it local to the EC2 instance or SageMaker notebook?
