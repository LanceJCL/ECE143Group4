import numpy as np
import pandas as pd
import sklearn as sk



df = pd.read_csv("H1B_dataset.csv", encoding='latin-1', low_memory=False, usecols=['CASE_SUBMITTED_YEAR','DECISION_YEAR', 'EMPLOYER_NAME', 'EMPLOYER_STATE', 'SOC_NAME', 'PREVAILING_WAGE', 'CASE_STATUS'])

df = df[df.CASE_SUBMITTED_YEAR.isin(range(2014,2019))]

print(df)
