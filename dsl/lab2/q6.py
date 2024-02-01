import pandas as pd
import numpy as np
df=pd.DataFrame({'Name':['A','B'], 'Quiz1':[9,8], 'Insem1':[14,13], 'Quiz2':[8,10], 'Insem2':[12,14]})
df['Total']=df[['Quiz1','Insem1','Quiz2','Insem2']].sum(axis=1)
df.loc['mean']=df[['Quiz1','Insem1','Quiz2','Insem2']].mean()
print(df)
