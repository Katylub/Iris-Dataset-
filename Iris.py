#Project 2019, Katylub Dona



# Import Data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the Data
f= pd.read_csv('IrisDataset.csv')

# Allow to see the for quickly testing if your object has the right type of data in it.
print (f.head())

# Check dimension dataset
print("The shape of dataset is:", (f.shape))

# Give description of dataset
print (f.describe())

#Check class
print(f.groupby('species').size())

#Univariable plot

# box and whisker plots
f.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# histograms
f.hist()
plt.show()

#Boxplot
f.boxplot(by='species')
plt.show()

#Scatter
pd.plotting.scatter_matrix(f)
plt.show()