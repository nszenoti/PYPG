# Drop irrelevant columns
df = df.drop(['ID', 'ZIPCode'], axis=1)

# Fix negative experience values
# Experience should logically be Age - Education years - 18
# (assuming education starts at age 18)
df['Experience'] = df['Age'] - 18
df.loc[df['Experience'] < 0, 'Experience'] = 0  # Set any negative values to 0

# ... existing code ...