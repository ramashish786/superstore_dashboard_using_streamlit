import pandas as pd
import matplotlib.pyplot as plt

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
df['Year'] = pd.DatetimeIndex(df['Order Date']).year
df['Month'] = pd.DatetimeIndex(df['Order Date']).month

df['Year-Month'] = df['Year'].astype(str) +'-'+  df['Month'].astype(str)


data = df[['Year-Month','Sales']].groupby(by=['Year-Month']).sum()['Sales']
data = data.reset_index()
plt.plot(data['Year-Month'],data['Sales'])
plt.show()
# data = data.unstack()


print(data.head())