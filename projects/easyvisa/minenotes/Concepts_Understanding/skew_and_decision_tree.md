No, **decision tree performance will not degrade** with log transformation, but it’s usually **unnecessary** for tree-based models. Here's why:  

### 🌳 **How Decision Trees Work**  
- Trees split data at specific thresholds (e.g., **no_of_employees > 5000**).  
- Log transformation **won’t change the relative order** of values—so splits remain the same.  
- However, **the depth & interpretability might change** because transformed values are harder to relate to the original scale.  

### 🔍 **When Log Transformation Might Hurt Trees**  
- If the data has **many repeated values** after log transformation, trees might lose granularity in splits.  
- If interpretability is important (e.g., “Company size > 10,000” is clearer than “log(company size) > 4”).  

### ✅ **Bottom Line**  
- **Not needed for trees** (they handle skew naturally).  
- **Useful for linear models** (like Logistic Regression).  
- **Won’t hurt trees significantly**, but may make splits harder to interpret.  

Do you want to keep it raw or try log transformation for curiosity? 🚀

---

Yes, absolutely! ✅  

For **visualization purposes**, applying a **log transformation** can help in:  
🔹 Making **histograms & box plots more interpretable** (spread values better).  
🔹 **Reducing the extreme peak** in skewed distributions.  
🔹 Helping detect patterns that might be **hidden due to extreme values**.  

It won’t affect the actual model training, but it makes plots more readable. So, for **EDA only**, log transformation is a great choice! 📊🔥  

Let me know if you want me to generate log-transformed visuals! 🚀