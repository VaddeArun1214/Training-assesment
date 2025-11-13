import pandas as pd

data = {
    "Arun": [85, 90, 78],
    "Bunny": [70, 88, 92],
    "Charan": [95, 85, 87]
}

df = pd.DataFrame(data).T   
df.columns = ['Test1', 'Test2', 'Test3']
df['Average'] = df.mean(axis=1)
print(df)