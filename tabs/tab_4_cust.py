import dash
from dash import dcc, html
import pandas as pd

tab_4_layout = html.Div([
    html.H3('How does a customer respond to a campaign?'),
    html.Div([
        html.Div('Select:', className='one column'),
        # Title,
        html.Div([
            html.Div('Education'),
            dcc.Dropdown(
                id='Education_dropdown',
                options=[{'label': j, 'value': i} for i,j in zip([0,1,2],['Graduate', 'PostGraduate', 'UnderGraduate'])],
                value='0',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Age'),
            dcc.Dropdown(
                id='Age_dropdown',
                options=[{'label': i, 'value': i} for i in range(20,80)],
                value='25',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Income'),
            dcc.Dropdown(
                id='Income_dropdown',
                options=[{'label': i, 'value': i} for i in range(1,670000)],
                value='75000',
                ),
        ],className='four columns'),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        html.Div([
            html.Div('Wine - Amt Spent'),
            dcc.Dropdown(
                id='MntWines_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 2600)],
                value='200',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Fruits - Amt Spent'),
            dcc.Dropdown(
                id='MntFruits_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 2600)],
                value='200',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Meat Products - Amt Spent'),
            dcc.Dropdown(
                id='MntMeatProducts_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 2600)],
                value='200',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Fish Products - Amt Spent'),
            dcc.Dropdown(
                id='MntFishProducts_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 2600)],
                value='200',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Sweet Products - Amt Spent'),
            dcc.Dropdown(
                id='MntSweetProducts_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 2600)],
                value='100',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Gold Products - Amt Spent'),
            dcc.Dropdown(
                id='MntGoldProds_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 2600)],
                value='500',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Past Month Num Deals Purchases'),
            dcc.Dropdown(
                id='NumDealsPurchases_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 10)],
                value='5',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Past Month Num Web Purchases'),
            dcc.Dropdown(
                id='NumWebPurchases_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 10)],
                value='5',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Past Month Num Catalog Purchases'),
            dcc.Dropdown(
                id='NumCatalogPurchases_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 10)],
                value='5',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Past Month Num Store Purchases'),
            dcc.Dropdown(
                id='NumStorePurchases_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 10)],
                value='5',
            ),
        ], className='four columns'),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        html.Div([
            html.Div('Days since most recent purchase'),
            dcc.Dropdown(
                id='Recency_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 100)],
                value='30',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Number of Web visits per month'),
            dcc.Dropdown(
                id='Webvisits_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 20)],
                value='5',
            ),
        ], className='four columns'),
        html.Div([
            html.Div('Years as a customer'),
            dcc.Dropdown(
                id='customerSince_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 10)],
                value='2',
            ),
        ], className='five columns'),
        html.Div('     ', className='one column')
    ],className='twelve columns'),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div('Select:', className='one column'),
        html.Div([
            html.Div('Marital Status'),
            dcc.RadioItems(
                id='MaritalStatus_dropdown',
                options=[{'label': j, 'value': i} for i, j in zip([2, 1, 0], ['Single', 'Relationship','NewlySingle', ])],
                value='2',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Children in Household'),
            dcc.RadioItems(
                id='children_radio',
                options=[{'label': j, 'value': i} for i, j in zip([1, 0], ['Yes', 'No'])],
                value='0',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Responded to Campaign A'),
            dcc.RadioItems(
                id='priorCmpgnA_radio',
                options=[{'label': j, 'value': i} for i, j in zip([1, 0], ['Yes', 'No'])],
                value='0',
                ),
        ],className='five columns'),
        html.Div([
            html.Div('Responded to Campaign B'),
            dcc.RadioItems(
                id='priorCmpgnB_radio',
                options=[{'label': j, 'value': i} for i, j in zip([1, 0], ['Yes', 'No'])],
                value='0',
                ),
        ],className='five columns'),
        html.Div([
            html.Div('Responded to CampaignC'),
            dcc.RadioItems(
                id='priorCmpgnC_radio',
                options=[{'label': j, 'value': i} for i, j in zip([1, 0], ['Yes', 'No'])],
                value='0',
                ),
        ],className='five columns'),
    ],className='twelve columns'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    # Output results
    html.Div([
        html.Div(id='user-inputs-box', style={'text-align':'center','fontSize':18}),
        html.Div(id='final_prediction', style={'color':'red','text-align':'center','fontSize':18})
    ],className='twelve columns'),

])
