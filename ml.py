import numpy as np 
import pandas as pd 

pred= pd.Series(np.ones(5, dtype=int))
dead=[0,0,0,0,0]
print(pred)
print(pd.Series(dead))