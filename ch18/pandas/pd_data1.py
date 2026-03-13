# pd_data1.py

import pandas as pd

data = {
    'ID': [1,2,3],
    'NAME': ['Alice', "Bob", 'Charlie'],
    'AGE':[30,25,35]
}

df = pd.DataFrame(data)
print(df)
print(df['NAME']=='Bob')
print(df[df['NAME']=='Bob'])
print(df[df['AGE']>=30])

sorted_df = df.sort_values(by="AGE", ascending=False)
print(sorted_df)

df['SALARY'] = [50000, 60000, 70000]
print(df)

df.loc[len(df)] = [4,'David', 40, 80000]
print(df)

df = df.drop(0)
print(df)


data2 = {
    'ID': [5,6],
    'NAME': ["Eve", "Frank"],
    'AGE':[28, 33]
}

df2 = pd.DataFrame(data2)

concat_df = pd.concat([df, df2], axis=0, ignore_index=True)
print(concat_df)

df2 = df2.set_index('ID')
print(df2)

print("=======================")
data3 = {
    'ID': [1,2,3,4,5,6],
    'Department': ["HR", "Engineering", "Sales", 'R&D', 'Finance', "IT"],
}
df3 = pd.DataFrame(data3)

merged_df = pd.merge(concat_df, df3)
print(merged_df)

# dropna_df = merged_df.dropna()
# print(dropna_df)

meanval = merged_df["SALARY"].mean()
print(meanval)
merged_df['SALARY'] = merged_df['SALARY'].fillna(meanval)
print(merged_df)

print("=======================")

data4 = {
    'ID': [2,3],
    'NAME': ["Bob", 'Charlie'],
    'AGE':[25,35],
    'SALARY':[60000,70000],
    'Department':["Engineering", None]
}
df4 = pd.DataFrame(data4)
new_df = pd.concat([merged_df, df4])
print(new_df)

new_df = new_df.drop_duplicates()
print(new_df)
