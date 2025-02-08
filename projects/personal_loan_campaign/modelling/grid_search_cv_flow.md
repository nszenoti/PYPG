



If you're using GridSearchCV with `refit=True` (default), you DON'T need to fit again! Here's the correct way:

```python:projects/personal_loan_campaign/hw/notebook1.ipynb
# 1. Run GridSearchCV
grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=SEED),
    param_grid=param_grid,
    cv=5,
    scoring='f1'  # or whatever metric you choose
    # refit=True by default
)

# 2. This fit does everything: CV, finds best params, and refits on full training data
grid_search.fit(X_train, y_train)

# 3. Use best_estimator_ directly - NO NEED TO FIT AGAIN!
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("Best parameters:", grid_search.best_params_)
print("\nTest Set Performance:")
print(classification_report(y_test, y_pred))
```

The only time you need to fit again is if you create a new model with the best parameters:
```python
# This approach is unnecessary unless you have a specific reason
new_model = DecisionTreeClassifier(**grid_search.best_params_)
new_model.fit(X_train, y_train)  # Need to fit because it's a new model
```
