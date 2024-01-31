import folium as fp
import branca
import branca.colormap as cm
import seaborn as sns
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objects as go
from plotly import express as px
from matplotlib import legend
from folium import plugins


url = 'https://raw.githubusercontent.com/VicmanGT/KaggleCompetition/b39212ebd9c8106a00d7e9823183c6e7cb9305c6/Data/cities_air_quality_water_pollution.18-10-2021%20(1)%20with_coordiantes.csv'
df = pd.read_csv(url)
df.head()
df.drop(columns="Unnamed: 0", inplace=True)
df.shape
df.isnull().sum()

df.describe()
df.info()

df.duplicated().any()
# Un comment and run this bolck of code

# df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
# df = df.rename(columns=lambda x: x.replace('"', ''))
# df.to_csv("cities_air_quality_water_pollution.csv", index=False)

df = pd.read_csv("cities_air_quality_water_pollution.csv")
df.head()



# We Found no any outlier and no any missing values and its time to visualize it
df.head()
# Visualization
# Top 20 Water poluted Country
df.columns
df_top_20=df.groupby(' Country')[' WaterPollution'].mean().sort_values(ascending=True).head(20)
# df_top_20

fig = px.bar(df_top_20, x=df_top_20.index, 
             y=df_top_20,
             color=df_top_20.index)
fig.update_layout(xaxis_title='Countriies', 
                  yaxis_title = "Water Pollution",
                  title="Top 20 Water Popluted Countries"
                  )
fig.show()
# 
df.head()
# Top 20 countries with dirty air
df.columns
df_top_20_air = df.groupby(' Country')[' AirQuality'].mean().sort_values(ascending=False).head(20)
fig = px.bar(df_top_20_air, 
             x=df_top_20_air.values, 
             y=df_top_20_air.index,
             color=df_top_20_air.index,
             orientation='h')  

fig.update_layout(
    xaxis_title="Air Quality",
    yaxis_title="Country",
    title="Top 20 countries with dirty air",
    yaxis_categoryorder='total ascending' 
)

fig.show()

# 
df.head()

# Top 20 countries with clean air
df_top_20_Dirt_air = df.groupby(' Country')[' AirQuality'].mean().sort_values(ascending=True).head(20)
fig = px.bar(df_top_20_Dirt_air, 
             x=df_top_20_Dirt_air.index, 
             y=df_top_20_Dirt_air,
             color=df_top_20_Dirt_air.index,
            #  orientation='h'
            )  

fig.update_layout(
    xaxis_title="Air Quality",
    yaxis_title="Country",
    title="Top 20 countries with Clean air",
    yaxis_categoryorder='total ascending' 
)

fig.show()
# 
# Top 20 countries with Clean water
df.columns
df_top_20_water = df.groupby(' Country')[' WaterPollution'].mean().sort_values(ascending=False).head(20)

fig = px.bar(df_top_20_water, 
             x=df_top_20_water.index, 
             y=df_top_20_water,
             color=df_top_20_water.index, 
            #  orientation='h'
            )  

fig.update_layout(
    xaxis_title="Air Quality",
    yaxis_title="Country",
    title="Top 20 countries with Clean Water",
    yaxis_categoryorder='total ascending' ,
    height=400,
    width=800
)

fig.show()

# Top 20 countries with dirty water
df_top_20_Dwater = df.groupby(' Country')[' WaterPollution'].mean().sort_values(ascending=True).head(20)
fig = px.bar(df_top_20_Dwater, 
             x=df_top_20_Dwater.index, 
             y=df_top_20_Dwater,
             color=df_top_20_Dwater.index, 
            #  orientation='h'
            )  

fig.update_layout(
    xaxis_title="Air Quality",
    yaxis_title="Country",
    title="Top 20 countries with Dirty Water",
    yaxis_categoryorder='total ascending' ,
    height=400,
    width=800
)

fig.show()

#lets plot a line graph to compare between air polution and water polution in different countries
print(df_top_20_Dirt_air, df_top_20_Dwater)
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=df_top_20_Dwater, y=df_top_20_Dirt_air,
               mode='markers', marker= dict(color='orange')
               , marker_color = df_top_20_Dirt_air)
)
fig.update_layout(
    xaxis_title = "Water", yaxis_title = 'Air', 
    title = "Showing Realation bwtween Top 20 Country with Poluted Air and Water"
)
fig.show()
# ######
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=df_top_20_water, y=df_top_20_air,
               mode='markers', marker= dict(color='orange'),
                marker_color = df_top_20_water
                )
)
fig.update_layout(
    xaxis_title = "Water", yaxis_title = 'Air', 
    title = "Showing Realation bwtween Top 20 Country with Air and Water Quality"
)
fig.update_layout(height=500)
fig.show()
# 
#lets plot a heatmap of water and air
df.columns
water_air = [' AirQuality', ' WaterPollution']
df1 = df[water_air].corr()
# Plotting Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df1, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of the AirQuality and WaterPollution')
plt.show()

# Geovisualization
df.head()
map = fp.Map()
map = fp.Map(locations=[40.712728, -74.006015], zoom_start=4)