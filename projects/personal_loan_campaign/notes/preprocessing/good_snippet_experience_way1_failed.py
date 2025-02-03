# Calculate expected experience based on formula
expected_exp = df['Age'] - 18

# Create comparison dataframe
comparison_df = pd.DataFrame({
    'Age': df['Age'],
    'Actual_Experience': df['Experience'],
    'Expected_Experience': expected_exp,
    'Difference': df['Experience'] - expected_exp
})

# Basic statistics of the differences
print("Statistics of difference between actual and expected experience:")
print(comparison_df['Difference'].describe())

# Calculate percentage of people within different ranges
within_1_year = (abs(comparison_df['Difference']) <= 1).mean() * 100
within_2_years = (abs(comparison_df['Difference']) <= 2).mean() * 100
within_5_years = (abs(comparison_df['Difference']) <= 5).mean() * 100

print("\nPercentage of people with difference:")
print(f"Within ±1 year: {within_1_year:.2f}%")
print(f"Within ±2 years: {within_2_years:.2f}%")
print(f"Within ±5 years: {within_5_years:.2f}%")

# Show distribution of differences in ranges
print("\nDistribution of differences:")
print(pd.cut(comparison_df['Difference'],
            bins=[-float('inf'), -5, -2, -1, 1, 2, 5, float('inf')],
            labels=['< -5', '-5 to -2', '-2 to -1', '-1 to 1', '1 to 2', '2 to 5', '> 5'])
      .value_counts()
      .sort_index())