pipeline_benefits_plan

modeling approach with multiple models and sampling techniques, I recommend:

### Approach 1: Pipeline-based (recommended)
1. Create a base preprocessing pipeline that handles all encodings
2. Create separate model pipelines that include:
   - The preprocessing pipeline
   - Optional sampling step (None/SMOTE/undersampling)
   - The specific model (Decision Tree/Bagging/Random Forest)
3. This keeps everything organized and prevents data leakage

### Benefits of pipeline approach:
- Ensures consistent preprocessing across all models
- Prevents accidental data leakage
- Makes cross-validation cleaner
- Easier to compare models fairly
- More maintainable code

This approach lets you systematically compare all combinations (3 models × 3 sampling techniques) while ensuring preprocessing is applied consistently and correctly at each stage.
