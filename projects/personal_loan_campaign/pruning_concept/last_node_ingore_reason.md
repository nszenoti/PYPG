











The last element in the ccp_alphas sequence is typically removed because:

```python
# Example of ccp_alphas
path = dt.cost_complexity_pruning_path(X_train, y_train)
alphas = path.ccp_alphas[:-1]  # Remove last element
```

Reason:
1. The last alpha is the value needed to prune the root node
2. This would result in a tree with just one node (root)
3. Such a tree is useless - it just predicts the majority class

Example:
```
Sequence: [0, 0.02, 0.03, 0.05, 0.15]

α = 0.00: Full tree
α = 0.02: Some pruning
α = 0.03: More pruning
α = 0.05: Heavy pruning
α = 0.15: Just root node (remove this)
```

It's like:
- We want to find optimal pruning
- But not so much that we destroy the tree
- Last alpha would give a "non-tree" (just root)
- So we exclude it from consideration

That's why we typically use: `ccp_alphas[:-1]`
