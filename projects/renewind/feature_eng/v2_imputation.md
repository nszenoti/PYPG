Great follow-up — since you've seen the **distribution stats** of `V2`, here's the best strategy:

---

### ✅ Recommended Imputation for `V2`:

> 🟢 **Use Median Imputation**

---

### 💡 Why Median?

- **V2 is roughly symmetric**, but **still has a wide range** (from -12.3 to 13).
- **Median = 0.47**, very close to mean, so it won’t distort the central tendency.
- Median is also **robust to outliers**, which is safer than mean if we’re unsure about tail behavior.

---

### 🔁 Bonus:
If you later want to get fancier:
- Try **KNN imputer** or **Iterative Imputer** during preprocessing phase, especially if patterns between features matter.

But for now:
> ✅ **Stick with Median** — simple, clean, and fits the stats you've got.

Ready to move to plotting?