# pandas_module.py

import pandas as pd

data = [
    [1, 'Alice', 30], 
    [2, 'BOB', 25], 
    [3, 'Charlie', 35], 
]
df = pd.DataFrame(data, columns=[['id', 'name', 'age']])
print(df)
df = pd.DataFrame(data, columns=[['id', 'name', 'age']], index=['r1','r2','r3'])
print(df)


data = {
    'id': [1,2,3],
    'name': ['Alice', "BOB", 'Charlie'],
    'age':[30,25,35]
}

df = pd.DataFrame(data)
print(df)

