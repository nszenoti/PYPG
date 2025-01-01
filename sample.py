# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
# Replace 'your_dataset.csv' with the path to your dataset
df = pd.read_csv('your_dataset.csv')

# Step 3: Understand the data
print("Shape of the dataset:", df.shape)
print("Data types:\n", df.dtypes)
print("Summary statistics:\n", df.describe())

# Step 4: Data Cleaning
# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Handle missing values (example: fill with mean)
df.fillna(df.mean(), inplace=True)

# Check for duplicates
print("Number of duplicates:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Step 5: Data Visualization
# Distribution of numerical features
df.hist(bins=30, figsize=(20, 15))
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Pairplot for relationships between variables
sns.pairplot(df)
plt.show()

# Step 6: Feature Engineering (if necessary)
# Example: Create a new feature
# df['new_feature'] = df['feature1'] + df['feature2']

# Display the first few rows of the cleaned dataset
print("First few rows of the cleaned dataset:\n", df.head())