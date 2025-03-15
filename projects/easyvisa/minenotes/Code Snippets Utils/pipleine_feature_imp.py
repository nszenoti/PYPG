pipleine_feature_imp.py

# Get transformed column names
encoded_columns = ["education", "experience", "gender"]
passthrough_columns = ["age", "income"]  # Columns that were not transformed

final_columns = encoded_columns + passthrough_columns  # Maintain order

# Fit the model
pipeline.fit(X, y)

# Extract feature importance
importances = pipeline.named_steps["model"].feature_importances_

# Create a DataFrame for better readability
feature_importance_df = pd.DataFrame({
    "Feature": final_columns,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

print(feature_importance_df)


# -----

# - Helper to get name of columns ordered by pipleine

feature_names = preprocessor.get_feature_names_out()
clean_names = [name.split("__")[-1] for name in feature_names]
print(clean_names)  # ['education', 'experience', 'gender', 'age', 'income']
