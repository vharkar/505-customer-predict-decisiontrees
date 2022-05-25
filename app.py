import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import pickle
from tabs import tab_1_cust, tab_2_cust, tab_3_cust, tab_4_cust
from utils_cust import display_eval_metrics, Viridis


df=pd.read_csv('resources/final_probs_cust.csv')


## Instantiante Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config['suppress_callback_exceptions'] = True
app.title='Customer Predictions!'


## Layout
app.layout = html.Div([
    html.H1('Predicting Customer Responses'),
    dcc.Tabs(id="tabs-template", value='tab-1-template', children=[
        dcc.Tab(label='Introduction', value='tab-1-template'),
        dcc.Tab(label='Model Evaluation', value='tab-2-template'),
        dcc.Tab(label='Optimal Parameters', value='tab-3-template'),
        dcc.Tab(label='Predictions', value='tab-3-template'),
    ]),
    html.Div(id='tabs-content-template')
])


############ Callbacks

@app.callback(Output('tabs-content-template', 'children'),
              [Input('tabs-template', 'value')])
def render_content(tab):
    if tab == 'tab-1-template':
        return tab_1_cust.tab_1_layout
    elif tab == 'tab-2-template':
        return tab_2_cust.tab_2_layout
    elif tab == 'tab-3-template':
        return tab_3_cust.tab_3_layout
    elif tab == 'tab-4-template':
        return tab_4_cust.tab_4_layout
# Tab 2 callbacks

@app.callback(Output('page-2-graphic', 'figure'),
              [Input('page-2-radios', 'value')])
def radio_results(value):
    return display_eval_metrics(value)

@app.callback(Output('page-3-graphic', 'src'),
              Output('confusionM', 'figure'),
              [Input('page-3-radios', 'value')])
def radio_results(value):
    return display_eval_params(value), display_confusion_matrix('resources/roc_dict_B.json', 'resources/confusion_matrix_B.csv')

# Tab 4 Callback # 1
@app.callback(Output('user-inputs-box', 'children'),
            [
              Input('Education_dropdown', 'value'),
              Input('Age_dropdown', 'value'),
              Input('Income_dropdown', 'value'),
              Input('MaritalStatus_dropdown', 'value'),
              Input('customerSince_radio', 'value')
              Input('children_radio', 'value'),
                
              Input('Spending_dropdown', 'value'),
              Input('NumPurchases_dropdown', 'value'),

              Input('Webvisits_dropdown', 'value'),
              Input('Recency_dropdown', 'value'),
              Input('priorCmpgnA_radio', 'value'),
              Input('priorCmpgnB_radio', 'value'),
              Input('priorCmpgnC_radio', 'value'),

              ])
def update_user_table(edu, age, income, mstatus, recency, visits, children, customerSince, priorCmpgnA, priorCmpgnB, priorCmpgnC, spendingWine, spendingFruit, spendingMeat, spendingFish, spendingSweet, spendingGold, numStore, numDeals, numWeb, numCatalog):
    return html.Div([
        html.Div(f'Education: {edu}'),
        html.Div(f'Age: {age}'),
        html.Div(f'Income: {income}'),
        html.Div(f'Marital Status: {mstatus}'),
        html.Div(f'Children in household: {children}'),
        html.Div(f'Customer since (in years): {customerSince}'),
        html.Div(f'Amount Spent: {spending}'),
        html.Div(f'Number of Purchases: {nump}'),

        html.Div(f'Number of web visits: {visits}'),
        html.Div(f'Last Purchased (days ago): {recency} '),
        html.Div(f'Responded to Campaign A: {priorCmpgnA}'),
        html.Div(f'Responded to Campaign B: {priorCmpgnB}'),
        html.Div(f'Responded to Campaign C: {priorCmpgnB}'),
    ])

# Tab 4 Callback # 2
@app.callback(Output('final_prediction', 'children'),
            [
              Input('Education_dropdown', 'value'),
              Input('Age_dropdown', 'value'),
              Input('Income_dropdown', 'value'),
              Input('MaritalStatus_dropdown', 'value'),
              Input('Recency_dropdown', 'value'),
              Input('Webvisits_dropdown', 'value'),
              Input('children_radio', 'value'),
              Input('customerSince_radio', 'value'),
              Input('priorCmpgnA_radio', 'value'),
              Input('priorCmpgnB_radio', 'value'),
              Input('priorCmpgnC_radio', 'value'),
              Input('MntWines_dropdown', 'value'),
              Input('MntFruits_dropdown', 'value'),
              Input('MntMeatProducts_dropdown', 'value'),
              Input('MntFishProducts_dropdown', 'value'),
              Input('MntSweetProducts_dropdown', 'value'),
              Input('MntGoldProds_dropdown', 'value'),
              Input('NumDealsPurchases_dropdown', 'value'),        
              Input('NumWebPurchases_dropdown', 'value'),   
              Input('NumCatalogPurchases_dropdown', 'value'),   
              Input('NumStorePurchases_dropdown', 'value')
              ])
def final_prediction(edu, age, income, mstatus, recency, visits, children, customerSince, priorCmpgnA, priorCmpgnB, priorCmpgnC, spendingWine, spendingFruit, spendingMeat, spendingFish, spendingSweet, spendingGold, numStore, numDeals, numWeb, numCatalog):
    
    inputs=[income, children, recency, spendingWine, spendingFruit, spendingMeat, spendingFish, spendingSweet, spendingGoldmstatus, numDeals, numWeb, numCatalog, numSore, visits, priorCmpgnB, priorCmpgnA, priorCmpgnC, customerSince, age, edu, mstatus]
    
    keys=['Income', 'Teenhome', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 'AcceptedCmp3', 'AcceptedCmp5', 'AcceptedCmp2', 'Yrs_Customer', 'age', 'Education_', 'Marital_Status_']
    
    dictCust=dict(zip(keys, inputs))
    df=pd.DataFrame([dictCust])
    
    # create the features we'll need to run our logreg model.
    df['age']=pd.to_numeric(df.age, errors='coerce')
    
    df['Marital_Status_']=pd.to_numeric(df.Marital_Status, errors='coerce')
    df['Relationship']=np.where((df.Marital_Status=='Relationship'),1,0)
    df['NewlySingle']=np.where((df.Marital_Status=='NewlySingle'),1,0)

    df['Teenhome']=np.where((df.Children=='Yes'),1,0)
    
    df['AcceptedCmp2']=np.where((df.PriorCampaignC=='Yes'),1,0)
    df['AcceptedCmp3']=np.where((df.PriorCampaignB=='Yes'),1,0)
    df['AcceptedCmp5']=np.where((df.PriorCampaignA=='Yes'),1,0)
    
    df['Income']=pd.to_numeric(df.Income, errors='coerce')
    df['Recency']=pd.to_numeric(df.Recency, errors='coerce')
    df['Yrs_Customer']=pd.to_numeric(df.Yrs_Customer, errors='coerce')
    df['NumWebVisitsMonth']=pd.to_numeric(df.NumWebVisitsMonth, errors='coerce')
    
    df['MntWines']=pd.to_numeric(df.MntWines, errors='coerce')
    df['MntFruits']=pd.to_numeric(df.MntFruits, errors='coerce')
    df['MntMeatProducts']=pd.to_numeric(df.MntMeatProducts, errors='coerce')
    df['MntFishProducts']=pd.to_numeric(df.MntFishProducts, errors='coerce')
    df['MntSweetProducts']=pd.to_numeric(df.MntSweetProducts, errors='coerce')
    df['MntGoldProds']=pd.to_numeric(df.MntGoldProds, errors='coerce')
        
    df['NumStorePurchases']=pd.to_numeric(df.NumStorePurchases, errors='coerce')
    df['NumDealsPurchases']=pd.to_numeric(df.NumDealsPurchases, errors='coerce')
    df['NumWebPurchases']=pd.to_numeric(df.NumWebPurchases, errors='coerce')
    df['NumCatalogPurchases']=pd.to_numeric(df.NumCatalogPurchases, errors='coerce')

    df['Education_']=pd.to_numeric(df.Education_, errors='coerce')
    df['Graduate']=np.where(df.Education=='Graduate',1,0)
    df['PostGraduate']=np.where(df.Education=='PostGraduate',1,0)
    df['UnderGraduate']=np.where(df.Education=='UnderGraduate',1,0)

    # drop unnecessary columns, and reorder columns to match the model.
    
    df=df[['Income', 'Teenhome', 'Recency', 
           'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 
           'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 
           'AcceptedCmp3', 'AcceptedCmp5', 'AcceptedCmp2', 'Yrs_Customer', 'age', 'Education_', 'Marital_Status_']]

    # unpickle the final model
    file = open('resources/final_model.pkl', 'rb')
    model=pickle.load(file)
    file.close()
    
    # predict on the user-input values (need to create an array for this)

    prob=model.predict(df)
    final_prob=round(float(prob[0][1])*100,1)
    return(f'Probability of Responding: {final_prob}%')


####### Run the app #######
if __name__ == '__main__':
    app.run_server(debug=True)
