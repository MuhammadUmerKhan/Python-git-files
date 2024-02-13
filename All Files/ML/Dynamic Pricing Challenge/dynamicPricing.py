import plotly.express as px
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, ShuffleSplit, GridSearchCV
from sklearn.linear_model import LinearRegression

df = pd.read_csv("C:\DATA SCIENCE\Python-git-files\dataset\dynamic_pricing.csv")
df.shape
df.head()
df.describe()

df.isnull().sum()
# Outlier Treatment
df.head()
df['Location_Category'].unique()
df['Customer_Loyalty_Status'].unique()
df['Time_of_Booking'].unique()
df['Vehicle_Type'].unique()
df.info()

for i in df.columns:
    if df[i].dtype != 'object':
        df['Z_score'] = (df[i] - df[i].mean())/df[i].std()
        df = df[(df['Z_score']>-3) & (df['Z_score']<3)]
        df.drop(columns='Z_score', inplace=True)
df.shape

# Visualization
veh_eco = df.groupby(['Vehicle_Type'])['Historical_Cost_of_Ride'].mean()
fig = px.bar(x=veh_eco.index, y=veh_eco.values, title="Historical Cost of Ride on Vehicle type")
fig.update_layout(xaxis_title="Vehicle_Type", yaxis_title='Historical_Cost_of_Ride')
fig.show()

df.head()
df.drop(columns=["Number_of_Past_Rides", 'Location_Category', 'Customer_Loyalty_Status', 'Average_Ratings', 'Number_of_Past_Rides', 'Time_of_Booking'], inplace=True)
df.shape
df.head()
dummies = pd.get_dummies(df['Vehicle_Type'])
dummies = dummies.astype('int')
df = pd.concat([df, dummies], axis='columns')
df.head()
df.drop(columns='Vehicle_Type', inplace=True)
df.shape
df.columns

X = df.drop(columns='Historical_Cost_of_Ride')
X.head()
Y = df.Historical_Cost_of_Ride

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=10)
lr = LinearRegression()
lr.fit(x_train, y_train)
lr.score(x_test, y_test) # 0.8564418170605628
y_pre = lr.predict(x_test)

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
cros = cross_val_score(LinearRegression(), X, Y, cv = cv)
cros.mean() # 0.8787019090045523