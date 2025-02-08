













Yes, the effective penalty increases as we prune! Here's why:

```
Original Tree:
         A (α=0.05)
       /          \
    B (α=0.02)    C (α=0.03)
    /        \
D (leaf)    E (leaf)

Pruning Sequence:
1. First Prune (α > 0.02):
         A (α=0.05)
       /          \
    B (leaf)      C (α=0.03)

2. Next Prune (α > 0.03):
         A (α=0.05)
       /          \
    B (leaf)      C (leaf)

3. Final Prune (α > 0.05):
         A (leaf)
```

Why Penalty Increases:
1. Each pruning removes "weakest" subtrees first (lowest α)
2. Remaining subtrees have higher α values
3. Need higher ccp_alpha to prune them
4. Last remaining splits are the "strongest" (highest α)

It's like:
- First prune "cheap" splits (low penalty needed)
- Then "expensive" splits (higher penalty needed)
- Finally "crucial" splits (highest penalty needed)

That's why the sequence of alphas is always increasing!
