import numpy as np
import pandas as pd
import sklearn as sk



df = pd.read_csv("H1B_dataset.csv", encoding='latin-1', low_memory=False)

df = df[df.CASE_SUBMITTED_YEAR.isin(range(2014,2017))]


# df = df.rename(columns={'Unnamed: 0': 'ID'})

print(df)
