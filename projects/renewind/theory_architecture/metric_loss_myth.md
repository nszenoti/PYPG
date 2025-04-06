











Exactly right! The `metrics` parameter in Keras is completely separate from the optimization process:

- The `loss` function is what the model actually optimizes during training
- The `metrics` are only calculated and reported for monitoring purposes

So when you specify:
```python
model.compile(
    optimizer=opt,
    loss='binary_crossentropy',
    metrics=['recall', 'precision']
)
```

The model will:
1. Optimize the weights to minimize binary_crossentropy
2. Calculate and report recall and precision, but not use them for optimization

This is why class weights are so important - they modify how the loss function weighs different types of errors, allowing you to indirectly prioritize recall even while using standard loss functions.

---











Yes, exactly. Metrics in Keras are purely "read-only indicators" that:

1. Are calculated and reported during training
2. Help you monitor model performance
3. Do not influence the training process in any way
4. Have no effect on weight updates or optimization

The only thing that drives the actual learning process is the loss function (and any associated weights like class_weight). Metrics are simply there to give you visibility into how your model is performing according to different evaluation criteria.

This is why you can add or remove metrics without changing how your model learns - they're just different ways of measuring performance, not instructions for training.


---

Significance

You're right about that specific point - if you don't track a metric during training, you won't have its history for the validation set across epochs.

However, you can still calculate the final validation metrics after training:

````python
# Calculate validation metrics after training
val_pred = (model.predict(X_val) > 0.5).astype(int)
val_precision = precision_score(y_val, val_pred)
val_recall = recall_score(y_val, val_pred)
val_f2 = fbeta_score(y_val, val_pred, beta=2)

print(f"Validation Precision: {val_precision:.4f}")
print(f"Validation Recall: {val_recall:.4f}")
print(f"Validation F2 Score: {val_f2:.4f}")
````


What you'll miss is the epoch-by-epoch progression of those metrics during training, which can be useful for diagnosing overfitting or determining optimal training duration.

For this reason, it's generally good practice to include all metrics you might be interested in during model compilation, even if they don't affect training.
