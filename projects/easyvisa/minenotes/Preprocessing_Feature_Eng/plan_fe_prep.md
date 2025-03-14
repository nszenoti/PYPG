### Preprocessing & Feature Engineering Plan

#### Bucket 1: Before Train-Test Split
1. **Negative value treatment**
   - Fix negative employee counts (take absolute values or set minimum to 0)

2. **Datatype conversion**
   - Convert categorical columns to 'category' dtype for efficiency
   - Convert target variable to appropriate format (binary classification)

3. **Feature derivation**
   - Create company age feature (current year - yr_of_estab)
   - Create company size categories (binned from no_of_employees)
   - Create wage categories (binned from prevailing_wage)

4. **Basic data cleaning**
   - Handle any extreme outliers that are clearly errors
   - Check for and remove duplicates (if any)

#### Bucket 2: After Train-Test Split
1. **Categorical encoding**
   - One-hot encoding for nominal variables
   - Ordinal encoding for ordered categories (education)

2. **Missing value imputation**
   - Impute based on training set statistics only

3. **Outlier treatment**
   - Handle outliers in numerical features (if needed)

4. **Sampling techniques**
   - Address class imbalance if needed (SMOTE, class weights, etc.)

This approach ensures no data leakage while preparing the data for ensemble models.
