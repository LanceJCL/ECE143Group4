import numpy as np
import pandas as pd
import sklearn as sk


#df = pd.read_csv("H1B_dataset.csv", encoding='latin-1', low_memory=False, usecols=['CASE_SUBMITTED_YEAR','DECISION_YEAR', 'EMPLOYER_NAME', 'EMPLOYER_STATE', 'SOC_NAME', 'PREVAILING_WAGE', 'CASE_STATUS'])

df = pd.read_csv("totalnew.csv", encoding ='latin-1', low_memory = False)

totaldf = df.reset_index()
df = df[df.CASE_SUBMITTED_YEAR.isin(range(2014,2019))]
df = pd.read_csv('totalnew.csv',low_memory=False)
totaldfn = df.reset_index()
df = totaldfn.drop(['index'], axis=1)


print(df)
