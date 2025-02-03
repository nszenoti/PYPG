# ------------------------ #
# 1. Import Necessary Libraries
# ------------------------ #

# Data manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# For missing value visualization
import missingno as msno

# For statistical tests (optional)
from scipy import stats

# ------------------------ #
# 2. Global Options & Themes
# ------------------------ #

# Set pandas display options for better readability
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', 100)      # Show 100 rows by default

# Seaborn theme for consistent plotting style
sns.set(style="whitegrid")  # You can change it to darkgrid, ticks, etc.
plt.rcParams["figure.figsize"] = (12, 8)  # Set default figure size for plots
plt.rcParams["font.size"] = 14            # Set font size for readability

# ------------------------ #
# 3. Helper Functions
# ------------------------ #

# Helper function for quick DataFrame inspection
def quick_inspect(df):
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")

    print("DataFrame Summary:")
    print(df.info(), "\n")

    print("Descriptive Statistics:")
    print(df.describe(), "\n")

# Helper function for visualizing missing values
def visualize_missing_values(df):
    msno.matrix(df)
    plt.show()

# Helper function for plotting histograms for numerical columns
def plot_numerical_distribution(df, numerical_cols):
    for col in numerical_cols:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], kde=True, color='skyblue', bins=30)
        plt.title(f'Distribution of {col}')
        plt.show()

# Helper function for plotting categorical variables
def plot_categorical_distribution(df, categorical_cols):
    for col in categorical_cols:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=df[col], data=df, palette="Set2")
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=45)
        plt.show()

# Helper function for correlation heatmap
def plot_correlation_heatmap(df, numerical_cols):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df[numerical_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Heatmap")
    plt.show()

# Helper function for boxplots to detect outliers
def plot_boxplots(df, numerical_cols):
    for col in numerical_cols:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[col], color='lightcoral')
        plt.title(f'Boxplot of {col}')
        plt.show()

# ------------------------ #
# 4. Load Dataset
# ------------------------ #

# Replace with the actual path to your dataset
df = pd.read_csv('your_dataset.csv')

# ------------------------ #
# 5. Initial Inspection
# ------------------------ #
# Quick overview of the dataset (first 5 rows, types, and basic statistics)
quick_inspect(df)

# ------------------------ #
# 6. Missing Data Analysis
# ------------------------ #
print("Missing Values Summary:")
print(df.isnull().sum())

# Visualize missing data
visualize_missing_values(df)

# ------------------------ #
# 7. Data Types and Categorical Variables
# ------------------------ #

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
print(f"Categorical Columns: {categorical_cols}")

# Plot distributions of categorical variables
plot_categorical_distribution(df, categorical_cols)

# ------------------------ #
# 8. Numerical Variables Exploration
# ------------------------ #

# Identify numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
print(f"Numerical Columns: {numerical_cols}")

# Plot distributions of numerical variables
plot_numerical_distribution(df, numerical_cols)

# Correlation heatmap for numerical variables
plot_correlation_heatmap(df, numerical_cols)

# ------------------------ #
# 9. Outlier Detection
# ------------------------ #
# Visualize outliers using boxplots
plot_boxplots(df, numerical_cols)

# ------------------------ #
# 10. Feature Engineering (Optional)
# ------------------------ #

# Example: Encoding categorical variables (if necessary)
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])
    print(f"Encoded {col}:\n", df[col].head())

# ------------------------ #
# 11. Statistical Testing (Optional)
# ------------------------ #

# Example: Shapiro-Wilk test for normality
for col in numerical_cols:
    stat, p_value = stats.shapiro(df[col].dropna())
    print(f"\nShapiro-Wilk Test for {col}: Stat={stat}, P-value={p_value}")
    if p_value < 0.05:
        print(f"The distribution of {col} is not normal.\n")
    else:
        print(f"The distribution of {col} is normal.\n")

