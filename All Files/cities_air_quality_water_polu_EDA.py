import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objects as go
from plotly import express as px

url = 'https://raw.githubusercontent.com/VicmanGT/KaggleCompetition/b39212ebd9c8106a00d7e9823183c6e7cb9305c6/Data/cities_air_quality_water_pollution.18-10-2021%20(1)%20with_coordiantes.csv'
df = pd.read_csv(url)
df.head()
df.drop(columns="Unnamed: 0", inplace=True)
df.shape
df.isnull().sum()
df.to_csv("cities_air_quality_water_pollution.csv", index=False)

df = pd.read_csv("cities_air_quality_water_pollution.csv")
df.head()