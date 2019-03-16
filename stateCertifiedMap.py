import plotly
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import sklearn as sk


df = pd.read_csv("out.csv",low_memory=False)
stateCertification(df)


def stateCertification(df):
    '''
    Functions gives the state wise Certified applicants for US
    Input: dataframe with selected columns for analysis
    '''

    assert isinstance(df,dataframe)
    df2 = df.loc[df['CASE_STATUS'] == 'CERTIFIED']
    df2 = df2[['EMPLOYER_STATE','CASE_STATUS']]



    sf_stateCount = df2['EMPLOYER_STATE'].value_counts()

    df1 = pd.DataFrame(data=sf_stateCount.index, columns=['EMPLOYER_STATE'])
    df2 = pd.DataFrame(data=sf_stateCount.values, columns=['CERTIFIED_COUNT'])
    df_stateCount = pd.merge(df1, df2, left_index=True, right_index=True)


    for col in df_stateCount.columns:
        df_stateCount[col] = df_stateCount[col].astype(str)



    scl = [
        [0.0, 'rgb(240,50,60)'],
        [0.05, 'rgb(220,50,50)'],
        [0.1, 'rgb(200,50,40)'],
        [0.2, 'rgb(180,50,30)'],
        [0.5, 'rgb(100,50,20)'],
        [1.0, 'rgb(84,50,10)']
    ]

    df_stateCount['text'] = df_stateCount['CERTIFIED_COUNT']


    data = [go.Choropleth(
        colorscale = scl,
        autocolorscale = False,
        locations = df_stateCount['EMPLOYER_STATE'],
        z = df_stateCount['CERTIFIED_COUNT'].astype(int),
        locationmode = 'USA-states',

        marker = go.choropleth.Marker(
            line = go.choropleth.marker.Line(
                color = 'rgb(255,255,255)',
                width = 2
            )),
        colorbar = go.choropleth.ColorBar(
            title = "H1B - Certified Visas")
    )]


    layout = go.Layout(

        geo = go.layout.Geo(
            scope = 'usa',
            projection = go.layout.geo.Projection(type = 'albers usa'),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'), title="H1B Certified Applicants by State"
    )


    fig = go.Figure(data = data, layout = layout)
    # py.iplot(fig, filename = 'd3-cloropleth-map')


    plotly.offline.plot(fig, filename='applicants_certified.html')
