Example of the Process:
Step 1 (Fully Grown Tree)
No pruning yet → Tree is deep, complex, overfitting.
Step 2 (First Pruning)
Remove nodes with the smallest ccp_alpha → New tree is slightly smaller.
Step 3 (Second Pruning)
Remove next set of nodes with the next smallest ccp_alpha → Tree gets even smaller.
Step 4 (Keep Repeating)
Continue pruning iteratively until only the root node remains.
This gives us multiple versions of the tree, each corresponding to different levels of complexity.