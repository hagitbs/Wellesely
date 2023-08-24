# Merge dflocal and dfglobal to the same CSV file  
# Join 2 csv's
import pandas as pd 

df1 = pd.read_csv('agg_global.csv')
df2 = pd.read_csv('agg_global_chat.csv')
df3 = pd.read_csv('agg_global_human.csv')
print (df1)
merged_df = pd.merge(df1, df2, on='word',   how='outer')
print(merged_df) 
big_merged_df = pd.merge(merged_df, df3, on='word',   how='outer')
print(big_merged_df ) 
print (big_merged_df.columns)
 
big_merged_df.rename(columns={'word': 'word', 'Maxpos_x': 'POS','wordCount_x':'wordCount-Global', 'percent_of_total_x':'percent_of_total-Global',
                                              'Maxpos_y': 'POS-Chat','wordCount_y':'wordCount-Chat', 'percent_of_total_y':'percent_of_total-Chat', 
                                              'Maxpos':'POS-Human', 'wordCount':'wordCount-Human', 'percent_of_total':'percent_of_total-Human'}, inplace=True)

big_merged_df.to_csv('agg_merged_all.csv',  index=False)