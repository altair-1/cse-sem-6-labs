import pandas as pd
import numpy as np
dict1={'Name':['A','B','C'], 'Height':[180,183,190], 'Qualification':['UG','PG','UG']}
studentData= pd.DataFrame(dict1)
studentData.insert(1,"Address",['Dwarka', 'Gautam Nagar', 'Noida'])
print(studentData)
