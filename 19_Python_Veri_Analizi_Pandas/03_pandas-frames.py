import pandas as pd

# data
dataInfo = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
dic = {
    "Name" : ["Ahmet","Ali","Yağmur","Çınar"],
    "Grade" : [50,60,70,80]
}

dict_list = [
    {"Name":"Ahmet","Grade":50},
    {"Name":"Ali","Grade":60},
    {"Name":"Yağmur","Grade":70},
    {"Name":"Çınar","Grade":80},
]

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])


data = dict(apples = s1 , oranges = s2)

df = pd.DataFrame(data)
"""
    OUTPUT :        apples  oranges
                0       3        0
                1       2        3
                2       0        7
                3       1        2
"""


print(df)

print("******************")
print("******************")

# df = pd.DataFrame()
'''
    OUTPUT : Empty DataFrame
                Columns: []
                Index: [] 
'''

# df = pd.DataFrame([1,2,3,4])
'''
    OUTPUT :       0
                0  1
                1  2
                2  3
                3  4
'''


df = pd.DataFrame(dataInfo)
'''
    OUTPUT :           0   1
                0   Ahmet  50
                1     Ali  60
                2  Yağmur  70
                3   Çınar  80
'''


df = pd.DataFrame(dataInfo,columns=['Name','Grade'])
'''
    OUTPUT :          Name  Puan
                0   Ahmet   50
                1     Ali   60
                2  Yağmur   70
                3   Çınar   80
'''


df = pd.DataFrame(dataInfo,columns=['Name','Grade'],index=[1,2,3,4])
'''
    OUTPUT :          Name  Grade
                1   Ahmet   50
                2     Ali   60
                3  Yağmur   70
                4   Çınar   80
'''

df = pd.DataFrame(dataInfo,[1,2,3,4],['Name','Grade'])
'''
    OUTPUT :          Name  Grade
                1   Ahmet   50
                2     Ali   60
                3  Yağmur   70
                4   Çınar   80
'''


df = pd.DataFrame(dataInfo,[1,2,3,4],['Name','Grade'],dtype=float)
'''
    OUTPUT :          Name  Grade
                1   Ahmet   50.0
                2     Ali   60.0
                3  Yağmur   70.0
                4   Çınar   80.0
'''


df = pd.DataFrame(dic)
'''
    OUTPUT :          Name  Grade
                1   Ahmet   50
                2     Ali   60
                3  Yağmur   70
                4   Çınar   80
'''


df = pd.DataFrame(dic,index=['a','b','c','d'])
'''
    OUTPUT :          Name  Grade
                a   Ahmet   50
                b     Ali   60
                c  Yağmur   70
                d   Çınar   80
'''



df = pd.DataFrame(dict_list)
'''
    OUTPUT :          Name  Grade
                a   Ahmet   50
                b     Ali   60
                c  Yağmur   70
                d   Çınar   80
'''

df = pd.DataFrame(dict_list,index=["212","321","654","987"])
'''
    OUTPUT :          Name  Grade
                212   Ahmet   50
                321     Ali   60
                654  Yağmur   70
                987   Çınar   80
'''

print(df)