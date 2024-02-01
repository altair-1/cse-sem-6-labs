import pandas as pd
import numpy as np
df1=pd.DataFrame({'Name':['A', 'B']})
df2=pd.DataFrame({'Maths':[18,20], 'Physics':[20,19], 'Chemistry':[18,19], 'Biology':[19,20]})
dfNew=pd.concat([df1,df2],axis=1)
print(dfNew)
dfNew['Total']=df2['Maths']+df2['Physics']+df2['Chemistry']+df2['Biology']
print(dfNew)
