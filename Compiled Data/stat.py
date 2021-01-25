import requests
import json
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjliMTg1ZTI0M2Y1NWNhN2FhNDUzZTRjZWZiZjVjMjVlZDVhZTFmNjk2MmVkOGNmMjdlYzZiNDZmNjU5YjlhMzdmYjEwOTYyMjMyNjkzNzc5In0.eyJhdWQiOiI5ODFkMWU5OTRmNTI0ZmQ1ODVlNzI3ZmMwZTkzN2U0OSIsImp0aSI6IjliMTg1ZTI0M2Y1NWNhN2FhNDUzZTRjZWZiZjVjMjVlZDVhZTFmNjk2MmVkOGNmMjdlYzZiNDZmNjU5YjlhMzdmYjEwOTYyMjMyNjkzNzc5IiwiaWF0IjoxNjExNDU1OTkxLCJuYmYiOjE2MTE0NTU5OTEsImV4cCI6MTYxNDEzNDM5MSwic3ViIjoiMTE0NDY4MDQiLCJzY29wZXMiOltdfQ.Yfv1NeMMb-ETJ8sxBV56ewi82PYASIJ7gKjr-C_EFJQAyK7bvcoc-FMbXy2ib70889vSr-FUY45OnvR-ao_5dhOcwqe8NaIRlg6ohbdU-ScUhyfwHaYFiHK5RjH87HssNPvxTEi9kNUBlMW0MZyEq4jK5lzLYR1Z0ai6WREVVVsbpPaTjTs9BebtuVYHyAhxMvJOTggjLW388JhvEKve_3WDbpgALK8qZ8tCa0JjZslxL_OKf1p7y4OSwZ8uYKn5dCkgUlWF5QOJmH6UGOwgtxPUMciWo33B5zSlmcP4w5LC39cwTrQ0XfucMRZRJzTU4CReeurDX29dpBAY8hp2Sw"

shows_per_season = {}
total_popularity_per_season = {}
total_popularity_shows_per_season = {}
#tduration_per_season = {}

def request(url):
    response = requests.get("https://api.myanimelist.net/v2/" + url,
        headers={"Authorization" : "Bearer " + access_token})

    status_code = response.status_code
    if(status_code != 200):
        print("Fail to GET " + str(status_code) + " https://api.myanimelist.net/v2/" + url)
    return json.loads(response.text)


def populate_dict(low, high):
    for year in range(low, high):

        total_popularity_per_season[  (str(year) + " spring")  ] = 0
        total_popularity_per_season[  (str(year) + " summer")  ] = 0
        total_popularity_per_season[  (str(year) + " fall")  ] = 0
        total_popularity_per_season[  (str(year) + " winter")  ] = 0

        total_popularity_shows_per_season[  (str(year) + " spring")  ] = 0
        total_popularity_shows_per_season[  (str(year) + " summer")  ] = 0
        total_popularity_shows_per_season[  (str(year) + " fall")  ] = 0
        total_popularity_shows_per_season[  (str(year) + " winter")  ] = 0

        #shows_per_season[  (str(year) + " spring")  ] = 0
        #shows_per_season[  (str(year) + " summer")  ] = 0
        #shows_per_season[  (str(year) + " fall")  ] = 0
        #shows_per_season[  (str(year) + " winter")  ] = 0

        #tduration_per_season[  (str(year) + " spring")  ] = 0
        #tduration_per_season[  (str(year) + " summer")  ] = 0
        #tduration_per_season[  (str(year) + " fall")  ] = 0
        #tduration_per_season[  (str(year) + " winter")  ] = 0


file_movies = open("Compiled Data/anime_movie_datac.txt", "r")
file_shows =  open("Compiled Data/anime_show_datac.txt", "r")

populate_dict(1970, 2021)

def tally(file):
    line = file.readline()
    while line != '':
        # print(line, end='')

        tokens = line.split(" ")
        key = (str(tokens[1]) + " " + tokens[2])

        shows_per_season[key] += 1

        line = file.readline()

# tally(file_shows)
# tally(file_movies)

print("\n")

#for thing in shows_per_season:
    # print (str(thing) + "\t" +str(shows_per_season[thing]))
    # print (str(shows_per_season[thing]))

def request_popularity(id, key):
    json_data = request("anime/" + str(id) + "?fields=mean")

    print(" " + id)

    if "mean" in json_data:
        total_popularity_per_season[key] += json_data["mean"]
        total_popularity_shows_per_season[key] += 1

def tally_popularity(file):
    line = file.readline()
    while line != '':
        # print(line, end='')

        tokens = line.split(" ")
        key = (str(tokens[1]) + " " + tokens[2])

        print(key, end="")

        request_popularity(tokens[0], key)

        line = file.readline()

tally_popularity(file_movies)
tally_popularity(file_shows)

for thing in total_popularity_per_season:
    # print (str(thing) + "\t" +str(shows_per_season[thing]))
    print(str(total_popularity_per_season[thing]) + " " + str(total_popularity_shows_per_season[thing]))