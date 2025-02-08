





Your reasoning about using recall is very good! Let's analyze why:

For imbalanced data (90% No, 10% Yes for loan):

1. **Why Recall is good choice here:**
   - Recall = TP/(TP+FN)
   - Focuses on minimizing False Negatives
   - In our case, False Negative = Customer would take loan but we didn't identify them
   - Cost of missing potential customer (FN) > Cost of approaching non-interested customer (FP)
   - Especially important since we have very few positive cases (10%)

2. **Why other metrics might not be as suitable:**
   - Accuracy: Would be misleading (90% accuracy by just predicting "No" always)
   - Precision: Might be too conservative, missing potential customers
   - F1-score: While balanced, might not capture our business need

```python:projects/personal_loan_campaign/hw/notebook1.ipynb
# Using recall for GridSearchCV
grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=SEED),
    param_grid=param_grid,
    cv=5,
    scoring='recall',  # Focus on finding actual loan takers
    n_jobs=-1
)
```

Business perspective:
1. Missing a potential customer (False Negative) = Lost business opportunity
2. Approaching non-interested customer (False Positive) = Just marketing cost
3. Therefore, higher recall is more valuable than higher precision

Your intuition was correct! For this specific problem with:
- Highly imbalanced data
- Higher cost of missing positive cases
- Marketing context

Recall is indeed a suitable metric to optimize for.
