import pandas as pd
import numpy as np
# pip install matplotlib
import matplotlib 
import matplotlib.pyplot as plt

url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
# df = pd.read_csv(url,header=None)

# df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
# df[['State']]

# df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
# df.columns
# reset = ['First Name', 'Last Name', 'City', 'Location ','Area Code','State']
# df = df[reset]

df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df = df.transform(func = lambda x : x + 10)

result = df.transform(func = ['sqrt'])
df.loc[0:3]

df.loc[[0,2], "a" ]

df.iloc[[0,1,2], 1]