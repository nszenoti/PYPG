











Think of alpha as a "complexity tax rate":

1. **What Alpha Represents**:
   ```
   α = (Increase in Error) / (Decrease in Tree Size)
   ```
   - It's like "error cost per node"
   - Higher α = Higher "tax" on complexity

2. **How it Penalizes**:
   ```
   For a subtree decision:
   Benefit = Accuracy improvement
   Cost = α × (number of nodes)

   Keep subtree only if: Benefit > Cost
   ```

3. **Example**:
   ```
   Subtree improves accuracy by 2%
   Adds 4 nodes

   If α = 0.003:
   Cost = 0.003 × 4 = 0.012 (1.2%)
   2% > 1.2% → Keep subtree

   If α = 0.007:
   Cost = 0.007 × 4 = 0.028 (2.8%)
   2% < 2.8% → Prune subtree
   ```

So alpha is like:
- A tax rate on tree complexity
- Higher rates discourage complex trees
- Lower rates allow more splits
- Balances accuracy vs simplicity

That's why it's called "Cost Complexity" - it puts a cost on complexity!
