# Logistic Regression
import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
import scipy.optimize as opt
import matplotlib.pyplot as plt
import pylab as py
url ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/ChurnData.csv"
df = pd.read_csv(url)

# df.to_csv('ChurnData.csv', index=False)
churn_data = pd.read_csv("ChurnData.csv")

churn_data.head()