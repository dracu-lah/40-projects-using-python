import plotly.express as px
data = px.data.gapminder()
print(data.head())

px.scatter(data, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="country", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])