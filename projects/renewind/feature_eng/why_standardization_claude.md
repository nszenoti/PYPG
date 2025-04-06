









Given your context, **standardization** (z-score normalization) is the better choice for scaling because:

1. **Neural networks perform better with standardized inputs** - Features with mean 0 and standard deviation 1 help gradient-based optimization converge faster

2. **All features have negative values** - Min-max normalization would compress the range, potentially losing signal, while standardization preserves the relative distances

3. **Many features show approximately normal distributions** - Standardization is particularly appropriate for normally distributed data

4. **Unknown feature meanings** - Without domain knowledge about the features, standardization is a safer default as it's less affected by outliers than min-max scaling

5. **Binary classification with neural networks** - Standardized features typically work well for this task type

Implement standardization using:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Remember to fit the scaler only on training data and apply the same transformation to test data.
