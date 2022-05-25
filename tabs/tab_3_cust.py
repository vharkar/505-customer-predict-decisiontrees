import dash
from dash import dcc, html
import pandas as pd

choices=['Maximum Tree Depth',
'Maximum Sample Leafs',
'Maximum Sample Splits',
'Maximum Features',
'Confusion Matrix']

tab_3_layout = html.Div([
    html.H3('Optimal Parameters'),
    html.Div([
        html.Div([
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                id='page-3-radios',
                options=[{'label': i, 'value': i} for i in choices],
                value='Optimal Parameters'
            ),
        ],className='two columns'),
        html.Div([
            dcc.Graph(id='page-3-graphic')
        ],className='ten columns'),
    ], className='twelve columns')




])
