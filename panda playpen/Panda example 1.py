import numpy as np
import pandas as pd
df = pd.read_csv("C:\Users\smcsh\OneDrive\Documents\Cognixia\churn.csv")
df.shape
(10000, 14)
df.columns
Index(['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure',
       'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited'], dtype='object')
#step1 dropping 
df.drop(['RowNumber', 'CustomerId', 'Surname',
         'CreditScore'], axis=1, inplace=True)
df.shape
(10000, 10)
#step2 select columns while reading
df_spec = pd.read_csv("/content/churn.csv",
                      usecols=['Gender', 'Age', 'Tenure', 'Balance'])
df_spec.head()

df_partial = pd.read_csv("/content/churn.csv", nrows=5000)
df_partial.shape
(5000, 14)

df_sample = df.sample(n=1000)
df_sample.shape
(1000, 10)

df_sample2 = df.sample(frac=0.1)
df_sample2.shape
(1000, 10)

df.isna().sum()
missing_index = np.random.randint(10000, size=20)
df.loc[missing_index, ['Balance', 'Geography']] = np.nan
df.iloc[missing_index, -1] = np.nan
mode = df['Geography'].value_counts().index[0]
df['Geography'].fillna(value=mode, inplace=True)
