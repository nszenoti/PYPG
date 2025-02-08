
`cross_val_score` and F1 serve different purposes:

1. **cross_val_score**:
   - A method to evaluate model performance
   - Uses cross-validation (multiple train-test splits)
   - Can use any scoring metric (including F1)
   ```python
   from sklearn.model_selection import cross_val_score

   # Using F1 as metric in cross validation
   scores = cross_val_score(
       dt,
       X, y,
       cv=5,           # 5-fold CV
       scoring='f1'    # metric to use
   )

   # Returns array of 5 scores
   print(scores)        # [0.92, 0.94, 0.91, 0.93, 0.92]
   print(scores.mean()) # Average performance
   ```

2. **F1-score**:
   - A metric to measure performance
   - Balance between precision and recall
   - Single train-test split
   ```python
   from sklearn.metrics import f1_score

   # Calculate F1 on test set
   y_pred = dt.predict(X_test)
   f1 = f1_score(y_test, y_pred)
   ```

Key Difference:
- cross_val_score = HOW you evaluate
- F1 = WHAT you measure

Think of it as:
- cross_val_score is the "test method"
- F1 is the "grading system"
