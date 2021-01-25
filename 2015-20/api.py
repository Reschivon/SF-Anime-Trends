
import requests
import json


file_movies = open("anime_movie_data.txt", "a")
file_shows = open("anime_show_data.txt", "a")
errors = open("anime_error_data.txt", "a")

def open_files():
    file_movies = open("anime_movie_data.txt", "a")
    file_shows = open("anime_show_data.txt", "a")
    errors = open("anime_error_data.txt", "a")

def close_files():
    file_movies.close()
    file_shows.close()
    errors.close()


def register_movie(id, year, season, name, duration):
    line = (str(id) + " " + str(year) + " " + season + " " + str(duration) + " " + name ).encode("ascii", 'ignore')
    file_movies.write(str(line)[2: -1:] + "\n")

def register_show(id, year, season, name, episodes, duration):
    line = ( str(id) + " " + str(year) + " " + season + " " + str(episodes) + " " + str(duration) + " " + name ).encode("ascii", 'ignore')
    file_shows.write(str(line)[2: -1:] + "\n")

def register_error(id):
    errors.write("error " + str(id) + "\n")

def request(url):
    response = requests.get("https://api.myanimelist.net/v2/" + url,
        headers={"Authorization" : "Bearer " + access_token})

    status_code = response.status_code
    if(status_code != 200):
        print("Fail to GET " + str(status_code) + " https://api.myanimelist.net/v2/" + url)
    return json.loads(response.text)

def search(query):
    json_data = request("anime?q=" + query + "&limit=40")
    print(json_data)

def request_season(year, season):
    print("Seasonal: " + season + " of " + str(year))
    json_data = request("anime/season/" + str(year) + "/" + season + "?limit=500")

    print("In this season: " + str(len(json_data["data"])) + " anime")

    next = json_data["paging"]
    if(len(next) != 0 ):
        print("There is another page here")

    return json_data["data"]

def request_details_print(id):
    json_data = request("anime/" + str(id) + "?fields=title,num_episodes,average_episode_duration")

    print(json_data)

    name = json_data["title"]
    print(name)

    episodes = json_data["num_episodes"]
    if(episodes == 1):
        print ("Movie")
    else:
        print ("Show")

    avg_length = json_data["average_episode_duration"]
    print("Average Length (min): " + str(avg_length/60))

def request_details(id, year, season):
    json_data = request("anime/" + str(id) + "?fields=title,num_episodes,genres,average_episode_duration")

    # print(json_data)

    try:
        name = json_data["title"]
        avg_length = json_data["average_episode_duration"]
        episodes = json_data["num_episodes"]
        genres = json_data["genres"]
        
        hassf = False
        for node in genres:
            if node["name"] == "Sci-Fi":
                hassf = True
        
        if not hassf:
            return
    except:
        register_error(id)
        return

    print("\t" + name)

    if(episodes == 1):
        register_movie(id, year, season, name, avg_length)
    else:
        register_show(id, year, season, name, episodes, avg_length)


print()

#request_season(2017, "summer")
#request_details(27411)
#search("ghost in the shell")

def years(low, high):
    for year in range(low, high):

        for node in request_season(year, "spring"):
            request_details(node["node"]["id"], year, "spring")

        for node in request_season(year, "summer"):
            request_details(node["node"]["id"], year, "summer")

        for node in request_season(year, "fall"):
            request_details(node["node"]["id"], year, "fall")

        for node in request_season(year, "winter"):
            request_details(node["node"]["id"], year, "winter")

    close_files()

#1970, 1976
#1976, 1980
#1980, 1990
#years(1990, 2000)
# years(2000, 2005)


years(2015, 2020)
#years(2013, 2016)
#years(2016, 2020)
