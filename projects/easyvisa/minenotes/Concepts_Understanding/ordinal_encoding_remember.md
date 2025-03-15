ordinal_encoding_remember

`OrdinalEncoder` in **Scikit-learn** encodes values as **floating-point (double) numbers**, not integers.  

### **Example:**
```python
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

data = np.array([['cat'], ['dog'], ['bird'], ['dog'], ['cat'], ['bird']])

encoder = OrdinalEncoder()
encoded_data = encoder.fit_transform(data)

print(encoded_data)
```
**Output (floating-point values):**
```
[[1.]
 [2.]
 [0.]
 [2.]
 [1.]
 [0.]]
```

### **Why Floating-Point?**
- Scikit-learn treats transformations as **continuous operations**, ensuring compatibility with models that expect float inputs.
- If you need **integers**, you can convert them manually:
  ```python
  encoded_int = encoded_data.astype(int)
  print(encoded_int)
  ```

Would you like an alternative encoding method that preserves integers? 🚀