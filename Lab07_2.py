import plotly.express as px


df=px.data.gapminder()

fig=px.bar(
    df,
    x='country',
    y='lifeExp',#'gdpPercap',#'pop',
    color='country',
    range_y=[0,100],#[0,150000],#range_y=[0,1500000000],#range for y-axis
    animation_frame='year',
    animation_group='country',
)

fig.show()