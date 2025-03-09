Yes, correlation doesn’t matter much in Decision Trees (DT) because:

1️⃣ Trees split features one at a time, selecting the one that provides the highest information gain (Gini impurity/entropy).
2️⃣ If two features are highly correlated, the tree picks one and ignores the other (since they provide nearly the same information).
3️⃣ Once a feature is used in a split, the impurity of the correlated feature decreases, making it less likely to be chosen later.