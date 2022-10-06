import numpy as np

x = [215, 325, 185, 332, 406, 522, 412,614, 544, 421, 445, 408],

y = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1,19.4, 25.1, 23.4, 18.1, 22.6, 17.2]

matrix = np.corrcoef(x, y)

print(matrix)


import pandas as pd

data = {
    'x' : [45,37,42,35,39],
    'y' : [38,31,26,28,33],
    'z' : [10,15,17,21,12]
}

dataframe = pd.DataFrame(data,columns=['x','y','z'])
print("DataFrame is :  ")
print(dataframe)

matrix = dataframe.corr()
print("correlation matrix is :  ")
print(matrix) 
