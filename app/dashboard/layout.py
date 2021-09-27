from dash import dcc
from dash import html

layout = html.Div(id='main', children=[
    html.H1(id='username'),
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph'),
    dcc.Store(id='user-store'),
], style={'width': '500'})
