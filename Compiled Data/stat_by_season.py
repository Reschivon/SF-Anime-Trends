
shows_per_season = {}
#tduration_per_season = {}

def populate_dict(low, high):
    for year in range(low, high):

        shows_per_season[  (str(year) + " spring")  ] = 0
        shows_per_season[  (str(year) + " summer")  ] = 0
        shows_per_season[  (str(year) + " fall")  ] = 0
        shows_per_season[  (str(year) + " winter")  ] = 0

        #tduration_per_season[  (str(year) + " spring")  ] = 0
        #tduration_per_season[  (str(year) + " summer")  ] = 0
        #tduration_per_season[  (str(year) + " fall")  ] = 0
        #tduration_per_season[  (str(year) + " winter")  ] = 0


# file_movies = open("anime_movie_datat.txt", "r")
file_shows = open("Compiled Data/anime_show_datac.txt", "r")

populate_dict(1970, 2021)

line = file_shows.readline()
while line != '':
    # print(line, end='')

    tokens = line.split(" ")
    key = (str(tokens[1]) + " " + tokens[2])

    shows_per_season[key] += 1

    line = file_shows.readline()

print("\n")

prev_year = 1970
for thing in shows_per_season:
    toks = thing.split(" ")
    if toks[0] != prev_year:
        prev_year = toks[0]
        print("\n" + str(toks[0]) + ' ', end="")
    
    print (str(shows_per_season[thing]) + ' ', end="")
