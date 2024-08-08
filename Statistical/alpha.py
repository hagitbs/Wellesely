import numpy as np
import csv
import pandas as pd
import numpy as np
from scipy import stats

# Open the CSV file for reading 
df = pd.read_csv('/Users/hagitbenshoshan/Documents/Wellesley/Wellesely/Statistical/rel.csv' ) 
print(df.head())  # Display the first few rows of the DataFrame
item_means = df.mean()
respondent_means = df.mean(axis=1)
total_variance = df.var().sum()
variance_due_to_item_means = respondent_means.var() * len(df.columns) 

cronbach_alpha = (len(df.columns) / (len(df.columns) - 1)) * (
    1 - (variance_due_to_item_means / total_variance)
)

# Print the result
print("Cronbach's Alpha REL:", cronbach_alpha)

df = pd.read_csv('/Users/hagitbenshoshan/Documents/Wellesley/Wellesely/Statistical/ins.csv' ) 
print(df.head())  # Display the first few rows of the DataFrame
item_means = df.mean()
respondent_means = df.mean(axis=1)
total_variance = df.var().sum()
variance_due_to_item_means = respondent_means.var() * len(df.columns) 
print('Number of columns ' ,len(df.columns)) 
cronbach_alpha = (len(df.columns) / (len(df.columns) - 1)) * (
    1 - (variance_due_to_item_means / total_variance)
)

# Print the result
print("Cronbach's Alpha INS:", cronbach_alpha)