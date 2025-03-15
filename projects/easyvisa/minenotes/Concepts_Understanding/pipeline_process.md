pipeline_process.md

You're correct! The pipeline **does not store** the transformed dataset internally after `fit()`.  

### **What Happens Internally?**  
1. **Pipeline `fit()` is called**  
   - The `ColumnTransformer` **learns** how to transform the data (e.g., encodes categories).  
   - The `DecisionTreeClassifier` **learns** from the transformed data.  

2. **Transformed Data Handling**  
   - The transformed dataset **exists temporarily** in memory while training.  
   - Once the pipeline moves forward, it **does not store** the transformed data.  
   - Instead, it stores only the **fitted transformers** (e.g., `OrdinalEncoder` and `LabelEncoder`) so they can transform new data on demand.

3. **If You Want to Inspect the Transformed Data**  
   - You must manually call `preprocessor.transform(X)`.  
   - The pipeline does **not cache** the transformed dataset for later access.

### **Key Takeaways**  
- **Pipeline does not persist transformed data**—it transforms data when needed.  
- **Only the fitted transformers & model remain stored** after `fit()`.  
- **Each `fit()` or `predict()` recomputes transformations dynamically**.  

This keeps the pipeline memory-efficient and flexible. 🚀