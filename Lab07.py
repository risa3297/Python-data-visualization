import plotly.express as px


df=px.data.gapminder()

fig=px.scatter(
    df,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    color='country',
    hover_name='country',
    log_x=True,
    size_max=100,
    range_x=[200,50000],#Limit value range for x-axis
    range_y=[25,90],#Limit value range for y-axis
    animation_frame='year',# from years 1952 to 2007,55frames.
    animation_group='country',
)

fig.show()