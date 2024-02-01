import pandas as pd
import numpy as np
df=pd.DataFrame({'A':pd.Timestamp('20130102'),'B':np.array([3]*4,dtype='int32'),'C':pd.Categorical(['Male','Female','Male','Female'])})
print(df[df.A>0]) #will fetch all positive values of A column
#Include a 6th column (a categorical) character data
print(df['F']==['Male','Female','Female','Male','Female','Female'])
#Setting by assigning with a numpy array
print(df.loc[:,'D']==np.array([5]*len(df)))
#Which will replace the ‘D’, column with all 5
print(df.drop ('col_name', axis =1, inplace=True))
#will drop the column name specified in col_name
print(df.drop ('row_index', axis =0, inplace=True))
#will drop the row specified in row_index
