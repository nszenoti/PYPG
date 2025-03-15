imbalance_remember_step.md

You're absolutely right. For imbalanced datasets, these are important considerations:

1. `stratify=y` during train-test split (which we're doing now)
2. `class_weight='balanced'` during model training
3. `average='weighted'` when calculating metrics like precision, recall, and F1

I'll keep these in mind when we get to the modeling and evaluation stages. These approaches will help ensure the models properly account for the class imbalance rather than just optimizing for the majority class.
