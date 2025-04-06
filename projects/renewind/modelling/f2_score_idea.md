To compute the **F2 score** (a variant of F1 score that weights **recall more heavily**), you can use **`fbeta_score`** from **`sklearn.metrics`** with `beta=2`.

---

### ✅ Example:

```python
from sklearn.metrics import fbeta_score

# Ground truth (actual labels)
y_true = [0, 1, 1, 1, 0, 1, 0]

# Model predictions
y_pred = [0, 1, 0, 1, 0, 1, 1]

# F2 score (binary classification)
f2 = fbeta_score(y_true, y_pred, beta=2)

print("F2 Score:", f2)
```

---

### 📌 Notes:
- `beta=2` → recall is given **4x** more importance than precision.
- For **multi-class** or **multi-label**, you can specify `average='macro'`, `'micro'`, or `'weighted'`.

---

### ⚙️ For multi-class:

```python
fbeta_score(y_true, y_pred, beta=2, average='macro')
```

> Options for `average`:
- `'binary'` (default for binary classification)
- `'micro'` (global metrics)
- `'macro'` (unweighted mean per class)
- `'weighted'` (accounts for class imbalance)

---

Let me know your case (binary/multi-class, DataFrame vs arrays), and I’ll tailor the snippet!