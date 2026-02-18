import os
from dotenv import load_dotenv
import sys
import requests
import re
from tabulate import tabulate

load_dotenv()
api_key = os.getenv("WATCH_MODE_API")

class Movie:
    def __init__(self, movie=None, country=None, id=None):
        if movie:
            self.movie = movie
        if country:
            self.country = country
        self.id = id

    def __str__(self):
        if self.id:
            return f"You want to watch {self.movie} in {self.country}. Its ID is {self.id}"
        return f"You want to watch {self.movie} in {self.country} (ID couldnt be found)"

    def get_stream_id(self, api_key):
        self.id = self.find_movie_id(api_key)
        if not self.id:
            return None
        return self.id

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        if not movie:
            raise ValueError("You must enter a movie!")
        self._movie = movie

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        regex = "^[A-Z]{2}$"
        if not country:
            raise ValueError("You must enter a broadcasting country!")
        else:
            if re.fullmatch(regex, country):
                self._country = country
            else:
                raise ValueError("Country Tag must be 2 letters!")

    def find_movie_id(self, api_key):
        url = f"https://api.watchmode.com/v1/search/?apiKey={api_key}&search_field=name&search_value={self.movie}"
        try:
            response = requests.get(url)
            data = response.json().get("title_results", [])
            self.id = data[0]["id"] if data else None
            return self.id
        except requests.RequestException:
            print("Could not find ID")
            return None

    def get_stream_services(self, id, api_key):
        url = f"https://api.watchmode.com/v1/title/{self.id}/sources/?apiKey={api_key}&regions={self.country}"
        response = requests.get(url)
        return response.json()

def main():
    movie_stream = get_movie_info()
    movie_stream.find_movie_id(api_key)
    services = movie_stream.get_stream_services(movie_stream.id, api_key)
    if not services:
        sys.exit("Failed search")

    duplicate = set()
    table_contents = []
    for serv in services:
        name = serv.get("name", "Unknown")
        stype = serv.get("type", "Unknown")
        dupe = (name, stype)
        if dupe not in duplicate:
            price = serv.get("price")
            if price is None:
                price = "0"
            else:
                price = f"{price}"
            url = serv.get("web_url", "Unknown")
            table_contents.append([name, stype, price, url])
            duplicate.add(dupe)

    headers = ["Stream service", "Type", "Price", "URL"]
    print(tabulate(table_contents, headers=headers, tablefmt="simple_grid"))

def get_movie_info():
    obj = Movie()
    while True:
        try:
            obj.movie = input("What movie would you like to find the platform for: ").strip()
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            obj.country = input("What country are you streaming from: ").strip().upper()
            break
        except ValueError as e:
            print(e)
    return obj

if __name__ == "__main__":
    main()
