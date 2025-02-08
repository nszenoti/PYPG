Let me explain Cost-Complexity Pruning (ccp_alpha) in a simple way:

**Intuitive Explanation:**
1. Think of ccp_alpha as a "penalty for complexity"
   - Low alpha = Complex tree (many nodes)
   - High alpha = Simple tree (fewer nodes)

2. **Example:**
   - Imagine you're deciding whether to split a node:
   ```
   Alpha = 0 (No penalty):
   Parent Node (accuracy 90%)
   ├── Split to get: Left Node (92%), Right Node (91%)
   Decision: Split! (Even tiny improvement is accepted)

   Alpha = 0.02 (Some penalty):
   Parent Node (accuracy 90%)
   ├── Split to get: Left Node (92%), Right Node (91%)
   Decision: Don't split! (Small improvement not worth the complexity)
   ```

3. **Formula (simplified):**
   - Benefit = Improvement in accuracy
   - Cost = alpha × number of nodes added
   - Only split if: Benefit > Cost

**Finding the right alpha:**
```python
# 1. Get path of alphas
path = dt.cost_complexity_pruning_path(X_train, y_train)
alphas = path.ccp_alphas

# 2. Try different alphas
for alpha in alphas:
    dt_pruned = DecisionTreeClassifier(ccp_alpha=alpha)
    # Lower alpha = More complex tree
    # Higher alpha = Simpler tree
```

Think of it like:
- alpha = 0: "Split whenever there's any improvement"
- alpha = 0.01: "Split only if improvement is worth the added complexity"
- alpha = 1: "Almost never split" (very simple tree)

It's like paying a "tax" for each node you add to the tree!
