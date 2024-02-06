from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection  import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# Load heart disease dataset in pandas dataframe
df = pd.read_csv("heart.csv")
df.head()

df.describe()
df.shape
df.isnull().sum()
df.info()
for i in df.columns:
    if df[i].dtype == 'object':
        print(i+':', df[i].unique())

for i in df.columns:
    if df[i].dtype != 'object':
        print(i)

df.head()
min(df.Age)
# Treat Outliers
# Cholesterol outlier
z_score = (df['Cholesterol'] - df['Cholesterol'].mean())/df['Cholesterol'].std()
df['Z_score'] = z_score
df1 = df[(df['Z_score']>-3) & (df['Z_score']<3)]
df1.shape
df1.head()
df1.drop(columns='Z_score', inplace=True)
df.drop(columns='Z_score', inplace=True)
# MaxHR
z_score = (df1['MaxHR'] - df1['MaxHR'].mean())/df1['MaxHR'].std()
df1['Z_score'] = z_score
df2 = df1[(df1['Z_score']>-3) & (df1['Z_score']<3)]
df2.shape
df2.drop(columns='Z_score', inplace=True)

# RestingBP
z_score = (df2['RestingBP'] - df2['RestingBP'].mean())/df2['RestingBP'].std()
df2['Z_score'] = z_score
df3 = df2[(df2['Z_score']>-3) & (df2['Z_score']<3)]
df3.shape
df3.drop(columns='Z_score', inplace=True)
df3.head()
# FastingBS
z_score = (df3['FastingBS'] - df3['FastingBS'].mean())/df3['FastingBS'].std()
df3['Z_score'] = z_score
df4 = df3[(df3['Z_score']>-3) & (df3['Z_score']<3)]
df4.shape
df4.drop(columns='Z_score', inplace=True)
df4.head()

# Oldpeak
z_score = (df4['Oldpeak'] - df4['Oldpeak'].mean())/df4['Oldpeak'].std()
df4['Z_score'] = z_score
df5 = df4[(df4['Z_score']>-3) & (df4['Z_score']<3)]
df5.shape
df5.drop(columns='Z_score', inplace=True)
df5.head()


# No outlier
df5.to_csv("heart_No_Outlier.csv", index=False)
df = pd.read_csv("heart_No_Outlier.csv")
df.head()
df.shape