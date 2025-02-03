For the **negative values** in the **Experience** column, we need to consider a couple of strategies, based on the context:

1. **Check for Data Entry Errors**:
   - Negative values for experience typically don’t make sense unless it’s a data error. You could validate whether these values are legitimate (e.g., a typo during data entry).
   - If they are errors, **imputation** could be used to replace them with more reasonable values (e.g., the mean or median of the column, or even zero if it's logical for someone to have no experience).

2. **Impute with Median/Mean**:
   - If negative values are errors, a simple way is to replace them with the **mean** or **median** experience of the dataset. The median might be better here as it's less sensitive to outliers.

3. **Set to Zero**:
   - If the negative values indicate people who are new or in training, setting them to zero might be valid.

4. **Treat as a Separate Category (if meaningful)**:
   - If the negative values could indicate a special case (e.g., people who just started their job but haven't reached an official “experience” threshold), you could treat those as a **separate category**.

5. **Remove the rows**:
   - If you believe that these rows with negative values are outliers or data errors that cannot be salvaged, you could choose to **drop them**. However, this depends on how many rows are affected—if it’s a significant portion, dropping them might introduce bias.

6. **Flagging**:
   - Alternatively, you could **flag** those negative values as a separate feature (binary) to capture whether the experience is invalid or special.

Once you've decided on one of these methods, it'll be part of the preprocessing pipeline when you're cleaning up the data for modeling.

How does that sound for handling these negative values?