preprocessing_rule_of_thiumb_gist

ref: https://chatgpt.com/c/67d124e2-aa24-8008-a9ed-23870a2f0fc3

Yes! **All transformations (like encoding, imputing, and scaling) should be learned from the training set only and then applied to the test set** to prevent data leakage.  

---

### **🚀 Correct Order (Best Practice for ML Pipelines)**  

| Step | Task | Before/After Split | Notes |
|------|------|------------------|-------|
| 1️⃣ | Handle Missing Values (Imputation) | **Before** | Avoids errors in feature engineering |
| 2️⃣ | Treat Outliers & Noise | **Before** | Prevents extreme values from dominating |
| 3️⃣ | Feature Engineering | **Before** | Create new features before encoding |
| 4️⃣ | **Train-Test Split** ✅ | **Now!** | Prevents leakage in encoding & scaling |
| 5️⃣ | **Learn from Train Data:** Encoding & Imputation | **After** | Fit on train, apply on both train & test |
| 6️⃣ | **Feature Scaling** | **After** | Fit scaler on train, transform both sets |
| 7️⃣ | **Handle Class Imbalance (if needed)** | **After** | SMOTE/Undersampling should be done on train only |
| 8️⃣ | **Feature Selection** | **After** | Remove redundant features to prevent overfitting |

---

### **Key Points:**
✅ **Encoding, Scaling, and Imputation must be fitted on training data** and applied to test data.  
✅ **Train-test split should be done before learning any transformation.**  
🚫 **Never use test data information during preprocessing.**  

Would you like a practical example to reinforce this? 🚀

Got it! Here's the **general notion** to decide whether a step should be done **before or after splitting**:  

### **✅ Do Before Split (Affects Data, Not Just Model)**
- **Removing duplicates** → This is a dataset issue, not a modeling issue.  
- **Fixing incorrect values (e.g., typos, impossible values)** → Data cleaning, not model-dependent.  
- **Creating new features** → Feature extraction doesn’t rely on target values.  
- **Removing obvious outliers (e.g., sensor errors)** → Prevents corrupt data from influencing both sets.  

### **✅ Do After Split (Model-Specific Transformations)**
- **Imputation (Handling Missing Values)** → Because test data may have different missing patterns.  
- **Encoding categorical variables** → The model should only learn from training data to avoid leakage.  
- **Feature Scaling (Normalization, Standardization)** → Scaling parameters must be learned from training only.  
- **Feature Selection (if data-driven, e.g., based on correlation with target)** → Avoid using test data patterns.  
- **Handling Class Imbalance (Oversampling/SMOTE)** → Test set must remain untouched to reflect real-world scenarios.  

### **General Rule of Thumb**  
👉 If a step **modifies data structure** (like feature creation, duplicate removal), do it **before split**.  
👉 If a step **learns from data** (like encoding, scaling, imputation), do it **after split** using train only.  

Now, you don’t have to memorize—just ask: **"Is this step modifying data or learning from it?"** 🚀

---

### Missing Value Doubt

Good catch! Let me clarify.  

### **When to Handle Missing Values?**  
It depends on **why** you're handling them:  

✅ **Before Split:**  
- If you're **removing rows** with missing values (because they are irrelevant or too many missing).  
- If you're **filling missing values using external domain knowledge** (not based on data patterns).  

✅ **After Split (Using Train Data Only):**  
- If you're **learning imputation from data** (mean/median/mode, KNN imputation).  
- This is crucial because test data should not influence imputation values.  

### **Final Rule of Thumb:**  
👉 **If missing values are handled manually (like dropping rows), do it before.**  
👉 **If missing values are filled based on dataset patterns (like mean/median), do it after using only train data.**  

Hope that clears it up! 🚀