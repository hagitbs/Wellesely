import numpy as np
import pandas as pd

def krippendorff_alpha(data, dtype=np.float64):
    """
    Calculate Krippendorff's alpha for inter-rater reliability.
    
    Args:
        data (array-like): 2D array of shape (subjects, raters). Data can contain NaN values for missing ratings.
        dtype: Data type to which the array should be cast.
        
    Returns:
        float: Krippendorff's alpha
    """
    data = np.array(data, dtype=dtype)
    n_raters = np.sum(~np.isnan(data), axis=1)
    metric_var = np.var(data, axis=1, ddof=1) * (n_raters / (n_raters - 1))
    metric_mean = np.nanmean(data, axis=1)
    nom = np.sum(metric_var)
    
    rater_means = np.nanmean(data, axis=0)
    denom_var = np.var(rater_means) * data.shape[0]
    
    return 1 - (nom / denom_var)

# Read data from CSV file
# Assuming the CSV file has columns representing raters and rows representing subjects
# Missing values should be indicated by 'NaN'
df = pd.read_csv("/Users/hagitbenshoshan/Documents/Wellesley/Wellesely/Statistical/team5.csv")
print (df)
df = df.iloc[:, 2:]
print (df )
selected_columns = df.iloc[:, [0, 3, 6]]  # Selects the 1st, 3rd, and 5th columns


# Convert the DataFrame to a NumPy array for calculations
data_array = selected_columns.to_numpy()
print (selected_columns)
print (data_array)

data_array = np.array([
    [1, 2, 1, 1, 1],  # Ratings from different raters for subject 1
    [1, 2, 1, 1, 1],  # Ratings for subject 2 (last rating is missing)
    [1, 1, 1, 1, 1],  # Ratings for subject 3
    [1, 1, 1, 1, 1],  # Ratings for subject 4
])

print (data_array)
# Calculate Krippendorff's alpha
result = krippendorff_alpha(data_array)
print(f"Krippendorff's alpha: {result}")
