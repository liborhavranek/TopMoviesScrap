import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

film_names = soup.find_all(name="h3", class_="title")

films = []

for film in film_names:
	films.append(film.get_text())

films.reverse()

print(films)

with open("movies_list.txt","w", encoding="utf-8") as f:
	for item in films:
		f.write(f"{item}\n")
