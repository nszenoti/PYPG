Yes — exactly. What you’re observing **strongly supports using standardization** (e.g. `StandardScaler`) over normalization. Here’s why:

---

### ✅ Why Standardization Makes Sense Here:

1. **Presence of Negative Values**:
   Since your features have both positive and negative values (some heavily in the negative range), normalization (which scales to [0, 1]) would **squash the scale** awkwardly and distort relationships.

2. **Distribution Shape**:
   You already mentioned that many features are **normally distributed** or symmetric — perfect for standardization, which assumes a Gaussian-ish distribution.

3. **Neural Network Context**:
   Feedforward networks **perform better** when input features have **zero mean and unit variance** — they converge faster and avoid activation saturation (especially for ReLU/tanh).

4. **Relative Importance Preserved**:
   Standardization maintains the **relative structure and outliers** more gracefully than normalization, which can compress valuable information into a small range if there are extremes.

---

### ⚠️ When You Might Prefer Normalization Instead:

- Features are all **positive** and on different scales.
- Data is **not Gaussian** and has **bounded ranges** (e.g., pixel values in images).
- Using methods like **k-NN**, **distance-based models**, or **gradient-free methods**.

---

So in your case:
✅ **Standardization (`StandardScaler`) is the best and safe choice.**

Let me know if you want to apply it to training + testing datasets next.