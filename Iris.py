#Project 2019, Katylub Dona



# Read Iris Data Set File

import numpy as np
import pandas as pd

f= pd.read_csv('IrisDataset.csv')
df = pd.DataFrame(f)
r= df.describe('IrisDataset.csv')

print (r)