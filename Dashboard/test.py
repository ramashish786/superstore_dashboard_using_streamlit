import pandas as pd

data_file = "../Data/superstore.csv"

df = pd.read_csv(data_file,encoding='unicode_escape')



df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

list_columns = df.columns
print(list_columns)

# # Sales by ship mode
# data = df[['Ship Mode','Sales']].groupby(by='Ship Mode')['Sales'].sum()
# print(data)

# Sales by  country

data = df[['Category','Sales']].groupby(by='Category')['Sales'].sum()
print(data)