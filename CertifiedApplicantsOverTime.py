import plotly
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import sklearn as sk

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import flask
import pandas as pd
import time
import os

def doshApp():
    '''
    doshFrame module creates a web interactive framework where the user can select from dropdown menu.
    Gives a time series graph of number of certified applicants for that specific year

    '''


    server = flask.Flask('app')
    server.secret_key = os.environ.get('secret_key', 'secret')


    df = pd.read_csv("out.csv",low_memory=False)

    df = df.loc[df['CASE_STATUS'] == 'CERTIFIED']
    ########################################################################################
    sf_yearCount = df['year'].value_counts()

    df1 = pd.DataFrame(data=sf_yearCount.index, columns=['Year'])
    df2 = pd.DataFrame(data=sf_yearCount.values, columns=['Count'])
    df_yearCountAll = pd.merge(df1, df2, left_index=True, right_index=True)



    for col in df_yearCountAll.columns:
        df_yearCountAll[col] = df_yearCountAll[col].astype(str)

    df_yearCountAll = df_yearCountAll.sort_values('Year')

    df_yearCountAll.insert(loc=0, column='Type', value=['All', 'All', 'All', 'All'])



    #######################################################################################
    df2 = df.loc[df['JOB_TITLE'] == 'PROGRAMMER ANALYST']
    sf_yearCountProgram = df2['year'].value_counts()

    df1 = pd.DataFrame(data=sf_yearCountProgram.index, columns=['Year'])
    df2 = pd.DataFrame(data=sf_yearCountProgram.values, columns=['Count'])
    df_yearCountProgram = pd.merge(df1, df2, left_index=True, right_index=True)


    # df2.set_index(df1,inplace = True)

    for col in df_yearCountProgram.columns:
        df_yearCountProgram[col] = df_yearCountProgram[col].astype(str)

    df_yearCountProgram = df_yearCountProgram.sort_values('Year')

    df_yearCountProgram.insert(loc=0, column='Type', value=['Prg', 'Prg', 'Prg', 'Prg'])
    df_yearCountAll= df_yearCountAll.append(df_yearCountProgram)
    ############################################################################################

    #######################################################################################
    df3 = df.loc[df['JOB_TITLE'] == 'SOFTWARE ENGINEER']
    sf_yearCountSoftware = df3['year'].value_counts()

    df1 = pd.DataFrame(data=sf_yearCountSoftware.index, columns=['Year'])
    df2 = pd.DataFrame(data=sf_yearCountSoftware.values, columns=['Count'])
    df_yearCountSoftware = pd.merge(df1, df2, left_index=True, right_index=True)


    # df2.set_index(df1,inplace = True)

    for col in df_yearCountSoftware.columns:
        df_yearCountSoftware[col] = df_yearCountSoftware[col].astype(str)

    df_yearCountSoftware = df_yearCountSoftware.sort_values('Year')

    df_yearCountSoftware.insert(loc=0, column='Type', value=['soft', 'soft', 'soft', 'soft'])
    df_yearCountAll= df_yearCountAll.append(df_yearCountSoftware)
    ############################################################################################

    #######################################################################################
    df4 = df.loc[df['JOB_TITLE'] == 'ACCOUNTANT']
    sf_yearCountAcc = df4['year'].value_counts()

    df1 = pd.DataFrame(data=sf_yearCountAcc.index, columns=['Year'])
    df2 = pd.DataFrame(data=sf_yearCountAcc.values, columns=['Count'])
    df_yearCountAcc = pd.merge(df1, df2, left_index=True, right_index=True)


    # df2.set_index(df1,inplace = True)

    for col in df_yearCountAcc.columns:
        df_yearCountAcc[col] = df_yearCountAcc[col].astype(str)

    df_yearCountAcc = df_yearCountAcc.sort_values('Year')

    df_yearCountAcc.insert(loc=0, column='Type', value=['acc', 'acc', 'acc', 'acc'])
    df_yearCountAll= df_yearCountAll.append(df_yearCountAcc)
    ############################################################################################

    #######################################################################################
    df5 = df.loc[df['JOB_TITLE'] == 'ARCHITECT']
    sf_yearCountAr = df5['year'].value_counts()

    df1 = pd.DataFrame(data=sf_yearCountAr.index, columns=['Year'])
    df2 = pd.DataFrame(data=sf_yearCountAr.values, columns=['Count'])
    df_yearCountAr = pd.merge(df1, df2, left_index=True, right_index=True)


    # df2.set_index(df1,inplace = True)

    for col in df_yearCountAr.columns:
        df_yearCountAr[col] = df_yearCountAr[col].astype(str)

    df_yearCountAr = df_yearCountAr.sort_values('Year')

    df_yearCountAr.insert(loc=0, column='Type', value=['ar', 'ar', 'ar', 'ar'])
    df_yearCountAll= df_yearCountAll.append(df_yearCountAr)
    ############################################################################################

    print(df_yearCountAll)

    app = dash.Dash('app', server=server)

    app.scripts.config.serve_locally = False
    dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

    app.layout = html.Div([
        html.H1('Year Trend for H1B Applicants'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'All Applicants', 'value': 'All'},
                 {'label': 'Programmer Analyst', 'value': 'Prg'},
                {'label': 'Software Engineer', 'value': 'soft'},
                {'label': 'Accountant', 'value': 'acc'},
                {'label': 'Architect', 'value': 'ar'}
            ],
            value='All'
        ),
        dcc.Graph(id='my-graph')
    ], className="container")

    @app.callback(Output('my-graph', 'figure'),
                  [Input('my-dropdown', 'value')])

def update_graph(selected_dropdown_value):
    dff = df_yearCountAll[df_yearCountAll['Type'] == selected_dropdown_value]
    return {
        'data': [{
            'x': dff.Year,
            'y': dff.Count,
            'line': {
                'width': 4,
                'shape': 'straight'
            }
        }],
        'layout': {
            'margin': {
                'l': 30,
                'r': 20,
                'b': 30,
                't': 20
            }
        }
    }

if __name__ == '__main__':
    app.run_server()
    doshApp()
