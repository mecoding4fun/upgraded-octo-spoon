import random
import plotly.express as px
import statistics
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('data5.csv')

Avg = df['Avg Rating'].tolist()

f = ff.create_distplot([Avg],['Average Rating'])
f.show()

