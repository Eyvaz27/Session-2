import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
from collections import Counter
import statistics as st       # StatisticsError
sns.set() 

phrase = '''
Hello World,   How are   you?  My name is
is \" Eyvaz \". What is your name?   '''
# print(phrase)
# name = input('')
# greet = "Hi, {}"
# print(greet.format(name))

# print(phrase[0:3])
# print(len(phrase))
# print(phrase.strip())
# print(phrase.lower())
# print(phrase.upper())
# phrase = phrase.replace('World', 'Azerbaijan')
# print(phrase)
# print(phrase.split('\n'))
# print('Hello ' + 'World')
# sentence = 'He is {he} years old and she is {she} years old.'
# print(sentence.format(he = 10, she = 15))

# list1 = list(np.arange(1, 11)) 
# print(list1[1])
# print(list1[-1])
# print(list1[1:10:2])
# print(list1[-5:10])
# print(list1[::])
# print(list1[::-1])

# list1.append(11)
# list1.insert(0, -1)
# list2 = list(np.arange(60, 10, -10))
# list1.extend(list2)
# print(list1)
# print(list1.index(20))
# list1.remove(40)
# list1.pop(0)
# list1.sort()
# list1.reverse()
# del list1[0]   # 60 will be deleted
# print(list1)

# def func(x, y):
#     return 2*(x+y), (x*y)

# my_tuple = tuple(np.arange(1, 11))
# try:
#     my_tuple[1] = 3
# except TypeError:
#     print("'tuple' object does not support item assignment")

# perimeter, area = func(3, 4)
# # perimeter, _ = func(3, 4)
# # _, area = func(3, 4)
# # perimeter, area = area, perimeter   # Pythonic way to swap variables
# print(perimeter, area)

# my_dict = {'name' : 'Eyvaz', 'surname' : 'Najafli'}
# try:
#     street = my_dict['street']
# except KeyError:
#     print('Key Error raises')

# name = my_dict.get('name')
# street = my_dict.get('street')
# my_dict['street'] = 'Independance'
# items = my_dict.items()
# keys = my_dict.keys()      # Dictionary Keys are "immutable"
# print(type(keys))          # <class 'dict_keys'>
# values = my_dict.values()

# for i, j  in zip(keys, values):
#     print(i + " : " + j)


# sentence = 'Hello World Hello Azerbaijan Hello World'
# s_list = sentence.split(' ')
# word_counts = Counter([])   # Counter accept "list" object
# for word in s_list:
#     word_counts[word]+=1
# for i in word_counts:
#     print(i + " : " + str(word_counts[i]))
# print('Most common : ' + str(word_counts.most_common(1)))

# print(all([True, 6.7, 'Hello']))
# print(all([None, 6.7, 'Hello']))
# print(any([None, 0, 'a']))

data = pd.read_csv('bank.csv')
# print(data.head(6))   # default is 5
# print(data.tail(6))     # default is 5
# print(data.shape)
# print(data.describe())
# print(data.mean())
# print(data.min())
# print(data.max())
# print(data.std())
# print(data.corr())
# print(data.count(numeric_only = True))  # Counts only numeric variables

# print(data.median())
# print(data[data['age']<30])
# data = data.sort_values(by = ['age'], kind = 'quicksort')
print(data)
# print(data.groupby(['age', 'job']).mean())
# print(pd.isnull(data).sum())

# data = data.dropna(how = 'all')
# data = data.fillna(0)
# print(data)
#
# data.columns = ['age', 'job', 'marital', 'study', 'def', 'balance', ...]
# print(data.columns)
#

mean = st.mean(data['age'])
print('Mean value for age -> {}'.format(mean))
