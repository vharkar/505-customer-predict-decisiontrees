import dash
from dash import dcc, html
import pandas as pd

choices3=['Maximum Tree Depth',
'Maximum Sample Leafs',
'Maximum Sample Splits',
'Maximum Features']

tab_3_layout = html.Div([
    html.H3('Optimal Parameters'),
    html.Div([
        html.Div([
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                id='page-3-radios',
                options=[{'label': i, 'value': i} for i in choices3],
                value='Maximum Tree Depth'
            ),
        ], className='two columns'),
        html.Div([
            html.Img(id='page-3-graphic', style={'height':'50%', 'width':'50%'})
        ], className='ten columns')
    ], className='twelve columns')




])
