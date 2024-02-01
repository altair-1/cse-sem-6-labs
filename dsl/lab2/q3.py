import pandas as pd
import numpy as np
dict1={'Name':['A','B','C'], 'Height':[180,183,190], 'Qualification':'UG'}
studentData= pd.DataFrame(dict1)
print(studentData)

list1=['Green Park', 'Shivaji Nagar', 'Tiger Circle']
studentData['Address']=list1
print(studentData)
