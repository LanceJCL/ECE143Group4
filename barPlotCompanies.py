import plotly
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
import sklearn as sk


df = pd.read_csv("out.csv",low_memory=False)
top5Certified(df)
top5Denied(df)

def top5Certified(df):
    '''
    Module for top 5 companies with the highest certified H1B applicants
    Input: df dataframe
    '''

    assert isintance(df,dataframe)

    df2 = df.loc[df['CASE_STATUS'] == 'CERTIFIED']
    df2 = df2[['EMPLOYER_NAME','CASE_STATUS']]


    sf_stateCount = df2['EMPLOYER_NAME'].value_counts()
    print(sf_stateCount)

    df1 = pd.DataFrame(data=sf_stateCount.index, columns=['EMPLOYER_NAME'])
    df2 = pd.DataFrame(data=sf_stateCount.values, columns=['DENIED_COUNT'])
    df_stateCount = pd.merge(df1, df2, left_index=True, right_index=True)


    for col in df_stateCount.columns:
        df_stateCount[col] = df_stateCount[col].astype(str)


    city_count  = sf_stateCount
    city_count = city_count[:5,]


    plt.figure(figsize=(15,10))
    sns.barplot(city_count.index, city_count.values, palette="Blues_d" ,alpha=0.8)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('Top 5 companies - Certified H1B', fontsize = 30)
    plt.ylabel('Number of Occurrences', fontsize=25)
    plt.xlabel('Company name', fontsize=25)
    plt.show()


def top5Denied(df):
    '''
    Module for top 5 companies with the highest denied H1B applicants
    Input: df dataframe
    '''

    assert isintance(df,dataframe)

    df2 = df.loc[df['CASE_STATUS'] == 'DENIED']
    df2 = df2[['EMPLOYER_NAME','CASE_STATUS']]


    sf_stateCount = df2['EMPLOYER_NAME'].value_counts()
    print(sf_stateCount)

    df1 = pd.DataFrame(data=sf_stateCount.index, columns=['EMPLOYER_NAME'])
    df2 = pd.DataFrame(data=sf_stateCount.values, columns=['DENIED_COUNT'])
    df_stateCount = pd.merge(df1, df2, left_index=True, right_index=True)


    for col in df_stateCount.columns:
        df_stateCount[col] = df_stateCount[col].astype(str)


    city_count  = sf_stateCount
    city_count = city_count[:5,]


    plt.figure(figsize=(15,10))
    sns.barplot(city_count.index, city_count.values,palette="Reds_d", alpha=1.0)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('Top 5 companies - Denied H1B', fontsize = 30)
    plt.ylabel('Number of Occurrences', fontsize=25)
    plt.xlabel('Company name', fontsize=25)
    plt.show()
