import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt



df = pd.read_csv("Master H1B Dataset.csv", encoding='latin-1', low_memory=False, usecols=['CASE_SUBMITTED_YEAR','DECISION_YEAR', 'EMPLOYER_NAME', 'EMPLOYER_STATE', 'SOC_NAME', 'PREVAILING_WAGE', 'CASE_STATUS'])

df1 = df[df.CASE_SUBMITTED_YEAR.isin(range(2014,2015))]
df2 = df[df.CASE_SUBMITTED_YEAR.isin(range(2015,2016))]
df3 = df[df.CASE_SUBMITTED_YEAR.isin(range(2016,2017))]
df4 = df[df.CASE_SUBMITTED_YEAR.isin(range(2017,2018))]

x=[2014,2015,2016,2017]
normals=[len(df1),len(df2),len(df3),len(df4)]
plt.plot(x, normals)
plt.show()