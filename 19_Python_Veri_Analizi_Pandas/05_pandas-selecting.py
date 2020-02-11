import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(3,3),index=['A','B','C',],columns=['Column1','Column2','Column3'])
result = df

result = df['Column1']
result = type(result)


result = df[['Column1','Column2']]

#   loc["row","column"] => loc["row"] => loc[":","column"]
result = df.loc['A']
result = df.iloc[2]  # C satırı gelir
result = type(result)

result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,"Column1":"Column2"]
result = df.loc[:,:"Column2"]


result = df.loc['A':'B',:"Column2"]
result = df.loc[:'B',:"Column2"]


result = df.loc["A","Column2"]
result = df.loc["C","Column1"]
result = df.loc[["A","B"],["Column1","Column2"]]


print(result)

df["Column4"] = pd.Series(randn(3),["A","B","C"])
print(df)
df["Column5"] = df["Column1"] + df["Column3"]
print(df)

result = df.drop('Column5',axis = 1)
print(df)
print(result)



df.drop('Column5',axis = 1, inplace=True)
print(df)