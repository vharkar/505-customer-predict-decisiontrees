import pandas as pd
import plotly
import plotly.graph_objs as go
import pickle
from sklearn.metrics import roc_auc_score
from tabs.tab_2_cust import choices2
from tabs.tab_3_cust import choices3
import json

Viridis = [
    "#440154", "#440558", "#450a5c", "#450e60", "#451465", "#461969",
    "#461d6d", "#462372", "#472775", "#472c7a", "#46307c", "#45337d",
    "#433880", "#423c81", "#404184", "#3f4686", "#3d4a88", "#3c4f8a",
    "#3b518b", "#39558b", "#37598c", "#365c8c", "#34608c", "#33638d",
    "#31678d", "#2f6b8d", "#2d6e8e", "#2c718e", "#2b748e", "#29788e",
    "#287c8e", "#277f8e", "#25848d", "#24878d", "#238b8d", "#218f8d",
    "#21918d", "#22958b", "#23988a", "#239b89", "#249f87", "#25a186",
    "#25a584", "#26a883", "#27ab82", "#29ae80", "#2eb17d", "#35b479",
    "#3cb875", "#42bb72", "#49be6e", "#4ec16b", "#55c467", "#5cc863",
    "#61c960", "#6bcc5a", "#72ce55", "#7cd04f", "#85d349", "#8dd544",
    "#97d73e", "#9ed93a", "#a8db34", "#b0dd31", "#b8de30", "#c3df2e",
    "#cbe02d", "#d6e22b", "#e1e329", "#eae428", "#f5e626", "#fde725"]


def display_roc(filename):
    with open(filename) as json_file:
        roc_dict = json.load(json_file)
        FPR = roc_dict['FPR']
        TPR = roc_dict['TPR']
        y_test = pd.Series(roc_dict['y_test'])
        predictions = roc_dict['predictions']

        roc_score = round(100 * roc_auc_score(y_test, predictions), 1)
        trace0 = go.Scatter(
            x=FPR,
            y=TPR,
            mode='lines',
            name=f'AUC: {roc_score}',
            marker=dict(color=Viridis[10])
        )
        trace1 = go.Scatter(
            x=[0, 1],
            y=[0, 1],
            mode='lines',
            name='Baseline Area: 50.0',
            marker=dict(color=Viridis[50])
        )
        layout = go.Layout(
            title='Receiver Operating Characteristic (ROC): Area Under Curve',
            xaxis={'title': 'False Positive Rate (100-Specificity)', 'scaleratio': 1, 'scaleanchor': 'y'},
            yaxis={'title': 'True Positive Rate (Sensitivity)'}
        )
        data = [trace0, trace1]
        fig = dict(data=data, layout=layout)
        return fig


def display_confusion_matrix(filename_roc, filename_confusion):
    with open(filename_roc) as json_file:
        roc_dict = json.load(json_file)
        FPR = roc_dict['FPR']
        TPR = roc_dict['TPR']
        y_test = pd.Series(roc_dict['y_test'])

        cm = pd.read_csv(filename_confusion)
        trace = go.Table(
            header=dict(values=cm.columns,
                        line=dict(color='#7D7F80'),
                        fill=dict(color=Viridis[55]),
                        align=['left'] * 5),
            cells=dict(values=[cm[f'n={len(y_test)}'], cm['pred: ignored'], cm['pred: responded']],
                       line=dict(color='#7D7F80'),
                       fill=dict(color='white'),
                       align=['left'] * 5))

        layout = go.Layout(
            title=f'Decision Tree Classifier',
        )

        fig = dict(data=[trace], layout=layout)
        return fig


def display_feature_importance(filename_fi):
    coeffs = pd.read_csv(filename_fi)
    # Let's display that with Plotly.
    mydata = [go.Bar(
        x=coeffs['feature'],
        y=coeffs['importance'],
        marker=dict(color=Viridis[::-6])
    )]

    mylayout = go.Layout(
        title='Feature Importance to the Model',
        xaxis={'title': 'Customer Feature'},
        yaxis={'title': 'Feature Importance'},

    )
    fig = go.Figure(data=mydata, layout=mylayout)
    fig


def display_classification_report(filename):
    cr = pd.read_csv(filename)
    trace = go.Table(
        header=dict(values=cr.columns,
                    line=dict(color='#7D7F80'),
                    fill=dict(color=Viridis[55]),
                    align=['left'] * 5),
        cells=dict(values=['', cr['precision'], cr['recall'], cr['f1-score'], cr['support']],
                   line=dict(color='#7D7F80'),
                   fill=dict(color='white'),
                   align=['left'] * 5))

    layout = go.Layout(
        title=f'Classification Report',
    )

    fig = dict(data=[trace], layout=layout)
    return fig


def display_eval_metrics(value):
    # Classification Report
    if value == choices2[0]:
        display_classification_report('resources/class_report_A.csv')

    # Receiver Operating Characteristic (ROC): Area Under Curve
    elif value == choices2[1]:
        display_roc('resources/roc_dict_A.json')

    # Confusion Matrix
    elif value == choices2[2]:
        display_confusion_matrix('resources/roc_dict_A.json', 'resources/confusion_matrix_A.csv')

    # Feature Importance
    elif value == choices2[3]:
        display_feature_importance('resources/feature_importance.csv')


def display_eval_params(value):
    # Maximum Tree Depth
    if value == choices3[0]:
        return './resources/max_depth.png'

    # Maximum Sample Leafs
    elif value == choices3[1]:
        return 'resources/min_samples.png'

    # Maximum Sample Splits
    elif value == choices3[2]:
        return 'resources/min_splits.png'

    # Maximum Features
    elif value == choices3[3]:
        return 'resources/max_features.png'
