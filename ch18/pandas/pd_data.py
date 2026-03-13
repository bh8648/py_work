# pd_data.py

import pandas as pd

df = pd.read_csv(r"./ch18/pandas/data.csv")

print(df)

print(df.sample(2))

print(df.sample(frac=0.5)) # 50%


