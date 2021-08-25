import pandas as pd


df = pd.read_csv('Sample_20210716.csv')
df.insert(3, "Load Detected", [0]*1432, True)
print(df.head())