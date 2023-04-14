import map
import pandas as pd
import chart_studio.tools
import plotly.io as pio
import plotly.express as px
import chart_studio.plotly as py

import sys
sys.path.append(r'C:\Users\ThinkBook\documents\myownwebsite')


username = 'angel_1234'
api_key = 'fioEJyuw1LxeFxva6phj'

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

countries_data = {
    'city': ['Washington DC', 'New York City', 'Paris'],
    'lat': [38.9072, 40.7128, 48.8566],
    'lon':  [-77.0369, -74.0060, 2.3522],
    'un-reported data of sexual violences': [0.77, 0.91, 0.90]
}

df = pd.DataFrame(countries_data)

fig = px.scatter_geo(df,
                     lat="lat",
                     lon="lon",
                     hover_name="city",
                     size="un-reported data of sexual violences",
                     projection="orthographic")

fig.update_layout(
    title={
        'text': "Un-reported data of sexual violence of women",
        'x': 0.5,
        'xanchor': 'center'
    }
)

fig.show()

py.plot(fig, filename='Map', config={
        'modeBarButtonsToRemove': ['sendDataToCloud']})
