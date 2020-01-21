import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Import data to notebook as "data":
data = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print(data.shape)
print(data[data['Price'] == data['Price'].max()])
#data[pd.isnull(data)]
# data.describe()
# print(data['Min.Price'].mean())
# print(data['Max.Price'].mean())
# data.columns

# print('First 5 row:')
# print(data.head())
# print('\nLast 5 row:')
# print(data.tail())

data['Min.Price'].fillna(data['Min.Price'].mean(), inplace = True, axis = 0)
data['Max.Price'].fillna(data['Max.Price'].mean(), inplace = True, axis = 0)
# print(data.loc[:, [3, 5]].mean())
# print(data.head())
# cols = list(data.columns)
# data = data[cols[0:4] + ['Max.Price'] + ['Average'] + ['Price'] + cols[7:-2]]
# data



