import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'values': [10, 20, 30, 40, 50]})

# Calculate the total sum
total_sum = df['values'].sum()

# Calculate the percentage of the total for each value
df['percent_of_total'] = (df['values'] / total_sum) * 100

print(df)