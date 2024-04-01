import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

df=px.data.gapminder()
print(df.columns)


data=dict(
    type='choropleth',
    locations=df['iso_alpha'],
    text=df['country'],
    colorscale='earth',
    z=df['lifeExp'],#df['pop'],#df['gdpPercap'],
    autocolorscale=False,
    reversescale=False,
    )
    
layout=dict(
    title='World Life Expectancy for year 1952 to 2007',
    geo=dict(
        showframe=False,
        projection={'type':'miller'}
    )

)

fig=go.Figure(data=[data],layout=layout)
fig.show()