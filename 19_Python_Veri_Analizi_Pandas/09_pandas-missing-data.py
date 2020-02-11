import pandas as pd
import numpy as np


data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(data, index=['a', 'c', 'e', 'f', 'h'], columns=[
                  'Column1', 'Column2', 'Column3'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
newColumn = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]
df["Column4"] = newColumn

result = df
result = df.drop("Column1", axis=1)
result = df.drop(["Column1", 'Column2'], axis=1)
result = df.drop('a', axis=0)
result = df.drop(['a', 'b', 'd', 'g'], axis=0)
result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df['Column1'].isnull()
result = df['Column1'].isnull().sum()
result = df['Column1'].isnull()
result = df[df['Column1'].isnull()]
result = df[df['Column1'].isnull()]["Column1"]
result = df[df['Column1'].notnull()]["Column1"]


result = df.dropna()    # varsayılan axis = 0 satıra göre çalışır
result = df.dropna(axis=1)
result = df.dropna(how="any")
result = df.dropna(how="all")
result = df.dropna(subset=["Column1", "Column2"], how="all")
result = df.dropna(subset=["Column1", "Column2"], how="any")
result = df.dropna(thresh=2)
result = df.dropna(thresh=4)
result = df.dropna(thresh=3)    # en az sayıda normal veri gelmeli örnek : 3

result = df.fillna(value="no input")
result = df.fillna(value=1)


def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value=ortalama(df))

print(result)
