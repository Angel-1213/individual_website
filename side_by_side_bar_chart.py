import side_by_side_bar_chart
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

risk_data = {
    'Risks': ['scared of walking in multistorey car parks', 'scared on waiting on train platforms', 'scared waiting at the bus stop', 'scared walking home from stop'],
    'Female': [0.62, 0.60, 0.49, 0.59],
    'Male': [0.31, 0.25, 0.20, 0.25]
}

df = pd.DataFrame(risk_data)

fig = px.histogram(df, x="Risks", y=['Female', 'Male'], barmode='group')

fig.update_layout(
    title={
        'text': "Difference on fear perception on women and men",
        'x': 0.5,
        'xanchor': 'center'
    },
    legend_title_text='Gender',
    yaxis_title="Probability of occurence"
)

fig.show()

py.plot(fig, filename='Graph', config={
        'modeBarButtonsToRemove': ['sendDataToCloud']})
