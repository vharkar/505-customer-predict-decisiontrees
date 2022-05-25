import dash
from dash import dcc, html
import pandas as pd

choices2=['Classification Report',
'ROC-AUC',
'Confusion Matrix',
'Feature Importance']

tab_2_layout = html.Div([
    html.H3('Model Evaluation'),
    html.Div([
        html.Div([
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                id='page-2-radios',
                options=[{'label': i, 'value': i} for i in choices2],
                value='ROC-AUC'
            ),
        ],className='two columns'),
        html.Div([
            dcc.Graph(id='page-2-graphic')
        ],className='ten columns'),
    ], className='twelve columns')

])
