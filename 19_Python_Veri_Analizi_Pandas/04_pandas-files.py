import pandas as pd
import sqlite3

df = pd.read_csv('19_Python_Veri_Analizi_Pandas/datasets/sample.csv')
print(df)


df = pd.read_json("19_Python_Veri_Analizi_Pandas/datasets/sample.json",encoding="utf-8")
print(df)

df = pd.read_excel("19_Python_Veri_Analizi_Pandas/datasets/sample.xlsx")
print(df)

connection = sqlite3.connect('19_Python_Veri_Analizi_Pandas/datasets/sample.db')
df = pd.read_sql_query("SELECT * FROM students",connection)
print(df)