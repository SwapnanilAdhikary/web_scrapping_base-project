import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
movie_Html = response.text
soup = BeautifulSoup(movie_Html,"html.parser")
#print(soup.prettify())
all_movies = soup.find_all(name="h3",class_="listicleItem_listicle-item__title__BfenH")
movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]

with open("movie.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")