#binning_no_employee.py

# Create company size categories
bins = [0, 10, 100, 1000, 10000, 100000, float("inf")]
labels = [
    "Micro (<10)",
    "Very Small (10-99)",
    "Small (100-999)",
    "Medium (1K-10K)",
    "Large (10K-100K)",
    "Very Large (>100K)",
]

# Create new binned feature
column_company_size = pd.cut(
    df["no_of_employees"].clip(lower=0), bins=bins, labels=labels
)