import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
url = "C:\DATA SCIENCE\Python-git-files\All Files\movies.csv"
df = pd.read_csv(url)

df.shape
df.describe()
df.head()
new_order = ['budget', 'company', 'country', 'director', 'genre', 'gross', 'name', 'rating', 'released', 'runtime', 'score', 'star', 'votes', 'writer', 'year']
df = df[new_order]
df['runtime']
df.head()
df.columns

# Cleaning Data
# Checking if there is any missing data
for col in df.columns:
    missing_data = np.mean(df[col].isnull())
    print('{}\t{}'.format(col, missing_data))

df['budget'].isnull().sum()
mean_budget = df['budget'].mean()
df['budget'].replace(np.NaN, mean_budget, inplace=True)
df['budget'].isnull().sum()

df['gross'].isnull().sum()
gross_mean = df['gross'].mean()
df['gross'].replace(np.NaN, gross_mean, inplace=True)

runtime_mean = df['runtime'].mean()
df['runtime'].isnull().sum()
df['runtime'].replace(np.NaN,runtime_mean, inplace=True)

score_mean = df['score'].mean()
df['score'].isnull().sum()
df['score'].replace(np.NaN,score_mean, inplace=True)

votes_mean = df['votes'].mean()
df['votes'].isnull().sum()
df['votes'].replace(np.NaN,score_mean, inplace=True)

df['writer']
df['released'].isnull().sum()
df['year'].isnull().sum()
df.dtypes
# change data type of columns
df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')
df['runtime'] = df['runtime'].astype('int64')
df['votes'] = df['votes'].astype('int64')
df.dtypes

df.sort_values(by=['gross'], inplace=False, ascending=False)
pd.set_option('display.max_rows', None)