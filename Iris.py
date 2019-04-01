#Project 2019, Katylub Dona



# Import Data

import numpy as np
import pandas as pd

#Read the Data
f= pd.read_csv('IrisDataset.csv')

# Allow to see the for quickly testing if your object has the right type of data in it.
print (f.head())

# Check dimension dataset
print("The shape of dataset is:", (f.shape))

# Give description of dataset
print (f.describe())