import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

with open(current_dir+"/movies.json","r") as file:
    movies = json.load(file)
print(movies)
print(movies[0]["title"]) 
print(movies[0]["director"]) 
print(movies[0]["year"]) 
print(movies[1]["title"]) 
print(movies[2]["title"])
print(movies[3]["title"])
