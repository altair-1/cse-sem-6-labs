import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Reading a CSV file & XLS file format
df = pd.read_csv('/home/210905282_drishaan/Documents/210905282_DSL/lab2/xyz.csv',header=None)
df.head() #This will display 1 st 5 records
df.tail() #This will display last 5 records
#The above dataset doesn’t have header, we shall attach our own header.
df.columns=['preg','glu','bp','sft','ins','bmi','dpf','age','class']
#Let us visualize the scatter plot of two continuous variable.
plt.scatter(df['bmi'],df['glu'])
plt.xlabel('bmi')
plt.ylabel('Glucose')
plt.show()
plt.hist(df['age'])
plt.show()
plt.boxplot(df['age'])
plt.show()
