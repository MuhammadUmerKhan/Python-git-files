from sklearn import svm
from cProfile import label
from turtle import color
import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/cell_samples.csv'
df = pd.read_csv(url)
df.head()
df.to_csv('cell_samples.csv', index=False)
df = pd.read_csv('cell_samples.csv')
# df.head()
df.drop(columns='Unnamed: 0', inplace=True)
df.head()
cell_df = df
cell_df.head()

cell_df.shape
cell_df.columns
cell_df.describe()
cell_df[['Class']]

ax = cell_df[cell_df['Class'] == 4][0:50].plot(kind='scatter', x='Clump', y='UnifSize', color='DarkBlue', label='malignant');
cell_df[cell_df['Class'] == 2][0:50].plot(kind='scatter', x='Clump', y='UnifSize', color='Yellow', label='benign', ax=ax);
plt.show()

# Data pre-processing and selectionc
cell_df.dtypes
cell_df[['BareNuc']]
# one row contain non numeric data now we are dropping this row
cell_df = cell_df[pd.to_numeric(cell_df['BareNuc'], errors='coerce').notnull()]
cell_df['BareNuc'] = cell_df['BareNuc'].astype('int')
cell_df.dtypes

feature_df = cell_df[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
feature_df.head()
x = np.asarray(feature_df)
x[0:5]

cell_df['Class'] = cell_df['Class'].astype('int')
y = np.asarray(cell_df['Class'])
y[0:5]

# Train/Test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
x_train.shape
x_test.shape
y_train.shape
y_test.shape

# Modeling (SVM with Scikit-learn)
clf = svm.SVC(kernel='rbf')
clf.fit(x_train, y_train)
yhat = clf.predict(x_test)
yhat[0:5]