import pandas as pd
import plotly.express as px

df=pd.read_csv('earthquakes-23k.csv')

fig=px.density_mapbox(
    df,
    lat='Latitude',
    lon='Longitude',
    z='Magnitude',
    radius=10,
    center=dict(lat=9,lon=9),
    zoom=1,
    color_continuous_scale='inferno',
    #autocolorscale=False,
    hover_name='Date',
    mapbox_style='stamen-watercolor',#'open-street-map',
    title='Earthquake events for years 1965 to 2016'
    )

fig.show()