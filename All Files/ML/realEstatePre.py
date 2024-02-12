import pandas as pd
import numpy as np

df = pd.read_csv("bengaluru_house_prices 2.csv")
df.head()
df.describe()
df.dtypes
df.shape
df.isnull().sum()

df['area_type'].unique()

df1 = df.drop(['area_type','society','balcony','availability'],axis='columns')
df1.head()

df1.isnull().sum()
df1.dropna(inplace=True)

# Feature Engineering
df1.head()
df1['BHK'] = df1['size'].apply(lambda x: int(x.split(' ')[0]))
df1.head()
df1.dtypes

# Explore total_sqft feature
def is_float(x):
    try:
        float(x)
    except:
        return False
    return True
df1[~df1['total_sqft'].apply(is_float)].head()

def convert_sqrt_num(x):
    token = x.split('-')
    if len(token) == 2:
        return (float(token[0])+float(token[1]))/2
    try:
        return float(x)
    except:
        return None
    
df2 = df1.copy()
df2.total_sqft = df2.total_sqft.apply(convert_sqrt_num)
df2 = df2[df2.total_sqft.notnull()]
df2
df2.dtypes

df3 = df2.copy()

df3['price_per_sqrt'] = df3['price']*100000/df3['total_sqft']
df3.head()

len(df3['location'].unique())

df3['location'] = df3['location'].apply(lambda x:x.strip())

location_stats = df3.groupby('location')['location'].agg('count').sort_values(ascending=False)
location_stats

len(location_stats[location_stats <= 10])

location_stats_less_than_10 = location_stats[location_stats <= 10]

len(df3['location'].unique())

df3.location = df3.location.apply(lambda x: 'other' if x in location_stats_less_than_10 else x)

len(df3['location'].unique())
df3.head()

