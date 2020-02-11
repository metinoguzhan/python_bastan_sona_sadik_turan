# themoviedb.org => film ve dizi arşivi
# themoviedb' nin sunduğu apiyi uygulamanızda kullanınız.
# anahtar kelimeye göre arama
# en popüler film listesi
# vizyondaki film listesi

import requests

class TheMovieDb:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3'
        self.api_key = 'apikey'
    
    def getPopulars(self,page):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page={page}")
        return response.json()
    
    def getTopRated(self,page):
        response = requests.get(f"{self.api_url}/movie/top_rated?api_key={self.api_key}&language=en-US&page={page}")
        return response.json()
    
    def getNowPlaying(self,page):
        response = requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page={page}")
        return response.json()
    def getSearchMovie(self,query,page):
        response = requests.get(f"{self.api_url}/search/company?api_key={self.api_key}&query={query}&page={page}")
        return response.json()

movieApi = TheMovieDb() 

while True:
    secim = input("1- Popular Movies\n2- Top Rated Movies\n3- Now Playing Movies\n4- Search Movies\n5- Exit\nSeçim: ")
    if secim == '5':
        break
    else:
        if secim == '1':
            page = int(input('page: '))
            movies = movieApi.getPopulars(page)
            for movie in movies['results']:
                print(movie['title'])
        elif secim == '2':
            page = int(input('page: '))
            movies = movieApi.getTopRated(page)
            for movie in movies['results']:
                print(movie['title'])
        elif secim == '3':
            page = int(input('page: '))
            movies = movieApi.getNowPlaying(page)
            for movie in movies['results']:
                print(movie['title'])
        elif secim == '4':
            keyword = input('keyword: ')
            page = int(input('page: '))
            movies = movieApi.getSearchMovie(keyword,page)
            for movie in movies['results']:
                print(movie['name'])
                
