### **Step-by-Step Guide to Implement Post-Pruning Using `ccp_alpha` in Decision Trees**

---

### **Step 1: Train a Fully Grown Decision Tree**
Train a decision tree without any pre-pruning restrictions (like `max_depth`, `min_samples_split`, etc.).

```python
from sklearn.tree import DecisionTreeClassifier

# Train a fully grown decision tree
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
```

---

### **Step 2: Get the Cost-Complexity Pruning Path**
Extract the `ccp_alphas` and corresponding impurity values.

```python
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities
```

> **Note:** `ccp_alphas` are sorted in **increasing order**, meaning smaller values result in **less pruning**, and higher values prune more aggressively.

---

### **Step 3: Train Multiple Trees for Different `ccp_alpha` Values**
Create and train decision trees for each `ccp_alpha`.

```python
clfs = []  # List to store trained models

for ccp_alpha in ccp_alphas[:-1]:  # Exclude last alpha (fully pruned tree)
    clf = DecisionTreeClassifier(random_state=42, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)
```

---

### **Step 4: Plot the Number of Nodes vs. `ccp_alpha`**
Check how pruning reduces tree complexity.

```python
import matplotlib.pyplot as plt

node_counts = [clf.tree_.node_count for clf in clfs]

plt.figure(figsize=(8, 5))
plt.plot(ccp_alphas[:-1], node_counts, marker="o", linestyle="--", color="b")
plt.xlabel("ccp_alpha")
plt.ylabel("Number of Nodes")
plt.title("Number of Nodes vs. ccp_alpha")
plt.show()
```

> **Interpretation:** As `ccp_alpha` increases, the number of nodes decreases, meaning the tree is getting pruned.

---

### **Step 5: Evaluate Each Pruned Tree**
Compare pruned trees using cross-validation.

```python
from sklearn.model_selection import cross_val_score
import numpy as np

train_scores = [cross_val_score(clf, X_train, y_train, cv=5, scoring="f1").mean() for clf in clfs]
test_scores = [cross_val_score(clf, X_test, y_test, cv=5, scoring="f1").mean() for clf in clfs]

plt.figure(figsize=(8, 5))
plt.plot(ccp_alphas[:-1], train_scores, marker="o", linestyle="--", label="Train", color="r")
plt.plot(ccp_alphas[:-1], test_scores, marker="o", linestyle="--", label="Test", color="g")
plt.xlabel("ccp_alpha")
plt.ylabel("F1 Score")
plt.title("F1 Score vs. ccp_alpha")
plt.legend()
plt.show()
```

> **Interpretation:**
> - Look for the `ccp_alpha` where **train and test scores are balanced** (avoiding overfitting or underfitting).
> - If the **test score increases and then drops**, choose the peak value.

---

### **Step 6: Select the Best `ccp_alpha` and Retrain Final Model**
Pick the `ccp_alpha` value with the best balance of performance and simplicity.

```python
optimal_alpha = ccp_alphas[np.argmax(test_scores)]
final_clf = DecisionTreeClassifier(random_state=42, ccp_alpha=optimal_alpha)
final_clf.fit(X_train, y_train)
```

---

### **Step 7: Visualize the Final Pruned Tree (Optional)**
```python
from sklearn.tree import plot_tree

plt.figure(figsize=(12, 8))
plot_tree(final_clf, filled=True, feature_names=X_train.columns, class_names=["Not Opted", "Opted"])
plt.show()
```

---

### **Summary of Steps**
1. Train a fully grown decision tree.
2. Get `ccp_alpha` values using `cost_complexity_pruning_path()`.
3. Train multiple decision trees for different `ccp_alpha` values.
4. Plot `ccp_alpha` vs. number of nodes to see pruning effect.
5. Evaluate models using cross-validation and select the best `ccp_alpha`.
6. Retrain the final decision tree with the optimal `ccp_alpha`.
7. Optionally visualize the final pruned tree.

---

This is the **complete procedure for post-pruning using `ccp_alpha`**. Let me know if you need any clarifications! 🚀