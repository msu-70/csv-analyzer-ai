import pandas as pd

result = pd.read_csv("sales.txt", sep="|", skiprows=[1])
result = result.dropna(axis=1, how="all")
result.columns = result.columns.str.strip()

result.to_csv("sales.csv", index=False)

