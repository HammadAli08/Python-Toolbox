import plotly.express as px
country=input("Enter the country code: ")
data={
    'country': [country],
    'value':[10]
}
Map = px.choropleth(
    data,
    locations='country',
    locationmode='country names',
    color='value',
    color_continuous_scale=px.colors.sequential.Blues,
    title=f'Map of {country}'
)
Map.show()