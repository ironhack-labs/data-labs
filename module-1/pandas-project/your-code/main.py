# Imported Libraries

import pandas as pd

# Importing CSV file into a data frame

shark_df = pd.read_csv('GSAF5.csv',encoding ='latin1')

shark_df_test = shark_df

# Shows the amount of null values in all columns

nulls = shark_df.isna().sum()
# print(nulls)

# print(nulls.loc['Area'])

# Drops columns with more than 1000 nulls

shark_df_test.dropna(axis = 1, thresh = len(shark_df_test) - 1000, inplace = True)

# for column in shark_df_test:
#     print(column)

#Drops any duplicate column

shark_df_test.drop_duplicates(inplace = True)

#Drops columns deemed not needed

shark_df_test.drop(['href formula','href', 'Case Number.1', 'Case Number.2', 'original order', 'Investigator or Source', 'Injury', 'pdf'], axis = 1, inplace = True)

# for column in shark_df_test:
#     print(column)

# Replace null values in FATAL columns with N

shark_df_test[['Fatal (Y/N)']] = shark_df_test[['Fatal (Y/N)']].fillna(axis = 0, value = 'N')

# Drop rows that have null values in Country column

shark_df_test.dropna(axis = 0, subset = ['Country'], inplace = True)

#Drop rows with type == Invalid

shark_df_test.drop(shark_df_test.loc[shark_df_test['Type']=='Invalid'].index, inplace=True)

# Replace any value in Type that are not Provoked with Unprovoked

shark_df_test.loc[(shark_df_test.Type != 'Provoked'),'Type']='Unprovoked'

# print(shark_df_test.Type.unique())

null_test = shark_df_test.isna().sum()
# print(null_test)

#Renaming Fatal column

shark_df_test.rename({'Fatal (Y/N)': 'Fatal'}, axis = 1, inplace = True)

nulls_1 = shark_df_test.isna().sum()

# Replacing values in Fatal with Yes or No

shark_df_test["Fatal"].replace(['N',' N', 'N ','n','UNKNOWN'], 'No', inplace = True) 

shark_df_test["Fatal"].replace('Y', 'Yes', inplace = True)

#Outputing CSV File

shark_df_test.to_csv('Clean_Data.csv', sep='\t', encoding='utf-8', index = False)

    
