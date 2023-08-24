#pip install pingouin
import pingouin as pg
import re
import pandas as pd

# Sample data
data = {
    'Rater1': [2, 3, 4, 5, 4],
    'Rater2': [3, 2, 4, 5, 6],
    'Rater3': [2, 3, 5, 4, 4]
}

df = pd.DataFrame(data)
print ( df )
# Calculate ICC
icc_data = pg.intraclass_corr(data=df, targets='Item', raters='Rater', ratings='Ratings',nan_policy='omit').round(3)
print(icc_data)
