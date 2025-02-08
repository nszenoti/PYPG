











Ah, let me clarify with a better example:

```
Original Tree:
         A
       /   \
      B     C
     / \
    D   E

Alpha calculations:
1. For D (leaf): No α (it's a leaf node)
2. For E (leaf): No α (it's a leaf node)
3. For subtree B (with D,E): α = 0.02
   - Compares accuracy of:
     * Using B as leaf vs
     * Using B with children D,E
4. For C (leaf): No α (it's a leaf node)
5. For whole tree (A): α = 0.05
   - Compares accuracy of:
     * Using A as leaf vs
     * Using A with children B,C
```

Sequence: [0, 0.02, 0.05]
- α = 0: Full tree
- α = 0.02: Prunes D,E (B becomes leaf)
- α = 0.05: Prunes B,C (A becomes leaf)

I apologize for my earlier confusion. Leaf nodes (D,E,C) don't get their own α values because:
1. They can't be pruned further
2. α is about the decision to keep/remove subtrees
3. Leaves have no subtrees to remove

The α values represent "pruning points" where subtrees are removed!
