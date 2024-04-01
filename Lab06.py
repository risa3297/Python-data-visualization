import pandas as pd
import plotly
import plotly.express as px

df=px.data.gapminder()
# print(df)
# print(df.columns)
# print(df.describe())

fig=px.scatter_geo(
    df,
    locations='iso_alpha',
    projection='orthographic',
    color='continent',
    opacity=0.8,
    hover_name='country',
    hover_data=['lifeExp','pop','gdpPercap'] )
    
fig.show()