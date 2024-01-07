import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

url = "C:\DATA SCIENCE\Python-git-files\dataset\movies.csv"
df = pd.read_csv(url)

df.shape
df.describe()

df.head()