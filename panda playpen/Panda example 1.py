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
