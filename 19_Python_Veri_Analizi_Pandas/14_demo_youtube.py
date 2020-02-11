import pandas as pd 

df = pd.read_csv("19_Python_Veri_Analizi_Pandas/datasets/youtube-ing.csv")
result = df
# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:15].head(5)


# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = len(df.columns)


# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)

result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","description","video_error_or_removed"],inplace=True,axis=1)
result = df

# 5- Beğenme (like) ve beğenmeme (dislikes) sayılarının ortalamasını bulunuz.
result = df["likes"].mean()
result = df["dislikes"].mean()


# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df[["title","likes","dislikes"]].head(50)
result = df.head(50)[["title","likes","dislikes"]]


# 7- En çok görüntülenen video hangisidir ?
result = df[df["views"].max() == df["views"]]["title"].iloc[0]



# 8- En düşük görüntülenen video hangisidir?
result = df[df["views"].min() == df["views"]]["title"].iloc[0]


# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values(by="views",ascending=False).head(10)[["title","views"]]


# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
# result = df.groupby("category_id")["likes"].mean().sort_values(axis = 0,ascending=False)
result = df.groupby("category_id").mean().sort_values("likes")["likes"]


# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
# result = df.pivot_table(index="category_id",values="comment_count",aggfunc="sum").sort_values("comment_count",ascending=False)
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]


# 12- Her kategoride kaç video vardır ?
result = df["category_id"].value_counts()


# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
# result = df["title"].str.len()
# df["str_len_info"] = df["title"].str.len()
# result = df

df["title_len"] = df["title"].apply(len)
result = df



# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# result = df["tags"].str.split("|").str.len().head(10)
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))

def tagCount(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tagCount)

result = df



# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)


def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste: 
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])

# print(result)