pipeline_transfoemd_dataset
---

Yes, you can extract the internally transformed dataset after fitting the pipeline.  

Since `Pipeline` applies transformations dynamically, you can access the preprocessed data like this:  

```python
X_transformed = pipeline.named_steps["preprocessor"].transform(X)
print("Transformed Data:")
print(X_transformed)
```

This ensures you're inspecting the actual transformed dataset that will be fed into the model. 🚀