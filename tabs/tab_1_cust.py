import dash
from dash import dcc, html
import base64

cust_photo=base64.b64encode(open('resources/customer-churn-edit.jpeg', 'rb').read())


tab_1_layout = html.Div([
    html.H3('Introduction'),
    html.Div([
    html.Div([
        dcc.Markdown("* Retrying Customer Predictions with DecisionTreeClassifier."),
        dcc.Markdown("* A predictive model that has been trained on a portion of the data, and tested on a set-aside portion."),
        dcc.Markdown("* Evaluation metrics showing the performance of the model on the testing data."),
        dcc.Markdown("* Determine optimal parameters for the model."),
        dcc.Markdown("* Use retrained classifier to make predictions based on user data."),
        html.A('View code on github', href='https://github.com/vharkar/505-customer-predict-decisiontrees'),
    ],className='ten columns'),
    html.Div([
    html.Img(src='data:image/jpeg;base64,{}'.format(cust_photo.decode()), style={'height':'400px'}),
    ],className='two columns'),


    ],className='nine columns'),

])
