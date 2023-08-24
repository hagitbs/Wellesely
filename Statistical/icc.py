#pip install pingouin
import pandas as pd
import pingouin as pg

# Create a sample DataFrame
data = {
    'Rater': ['R1', 'R1', 'R1', 'R2', 'R2', 'R2', 'R3', 'R3', 'R3'],
    'Subject': ['S1', 'S2', 'S3', 'S1', 'S2', 'S3', 'S1', 'S2', 'S3'],
    'Score': [8, 2, 6, 7, 3, 5, 9, 2, 7]
}

df = pd.DataFrame(data)
print (df) 
# Compute intraclass correlation
icc_df = pg.intraclass_corr(data=df, targets='Subject', raters='Rater', ratings='Score')

# Print the ICC results
print(icc_df)
