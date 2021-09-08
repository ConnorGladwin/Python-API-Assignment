import requests
import json
import random
from config import apiKey 

# API urls
imdbURL = "https://movie-database-imdb-alternative.p.rapidapi.com/"
utellyURL = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/idlookup"
# API headers
imdbHeaders = {
      'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
      'x-rapidapi-key': apiKey
    }
utellyHeaders = {
      'x-rapidapi-host': "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com",
      'x-rapidapi-key': apiKey
    }

# Searches for movie titles that match the user input name
class MovieSearch:
  def __init__(self, query):
    super().__init__()

    # Query parameters
    self.query = {"s": query, "plot": "short", "page": "1", "r": "json"}

    # API response
    res = requests.request("GET", imdbURL, headers=imdbHeaders, params=self.query).json()

    # Transforms the data to a state that we are able to parse
    json_string = json.dumps(res, indent=4)
    res_info = json.loads(json_string)
    i = 1

    if (res_info["Response"] == "True"):
      movieArray = []
      # Prints the title to the console if data is returned
      for movieTitle in res_info["Search"]:
        print("________________________________")
        print(i, ")", "Title: ", movieTitle["Title"])
        print(" - Year: ", movieTitle["Year"])
        WhereToWatch(movieTitle["imdbID"])
        print("________________________________")
        movieArray.append(movieTitle["imdbID"])
        i += 1
      while True:
        userSelect = input("Would you like more info about one of these movies? - Y|N: ")
        if (userSelect.upper() == "Y"):
          userSelect = input("Which movie would you like to know more about? Please input list number: ")
          print(MovieInfo(movieArray[int(userSelect) - 1]))
        elif (userSelect.upper() == "N"):
          break
        else:
          print("Invalid option selected")
          continue
    else: 
      print("We couldn't find the movie that you're looking for...")

# Find out where the movies can be watched
class WhereToWatch:
  def __init__(self, imdbID):
    super().__init__()

    # Query parameters
    querystring = {"source_id":imdbID, "source":"imdb", "country":"us"}

    # API response
    res = requests.request("GET", utellyURL, headers=utellyHeaders, params=querystring).json()

    # Transforms the data to a state that we are able to parse
    json_string = json.dumps(res, indent=4)
    res_info = json.loads(json_string)

    # Checks if the data within the returned dictionary contains data and prints if True
    if (len(res_info["collection"]) != 0):
      print(" - Where to watch it: ", res_info["collection"]["locations"][0]["display_name"])
      print(" - Link: ", res_info["collection"]["locations"][0]["url"])
    else:
      print("The universe obviously doesn't want you to watch this movie...")
      
# More info about the selected movie
class MovieInfo:
  def __init__(self, imdbID):
    super().__init__()

    # Query parameters
    self.query = {"type": "movie", "i": imdbID} 

    # API response
    res = requests.request("GET", imdbURL, headers=imdbHeaders, params=self.query).json()

    # Parses the dict returned from the API and transforms it to a string
    json_string = json.dumps(res, indent=4)
    res_info = json.loads(json_string)

    print("________________________________")
    print("Title: ", res_info["Title"])
    print(" - Year: ", res_info["Year"])
    print(" - Genre: ", res_info["Genre"])
    print(" - Runtime: ", res_info["Runtime"])
    print(" - Cast: ", res_info["Actors"])
    print(" - Plot: ", res_info["Plot"])
    print(" - Metascore: ", res_info["Metascore"])
    print("________________________________")

# Find a random movie
class FindSomethingRandom:
  def __init__(self):
    super().__init__()

    # Generates a random imdb id number
    imdbID = ('tt' + str(random.randint(0, 4)) + str(random.randint(111111, 999999)))

    # Query parameters
    self.query = {"type": "movie", "i": imdbID}

    # API response
    res = requests.request("GET", imdbURL, headers=imdbHeaders, params=self.query).json()

    # Parses the dict returned from the API and transforms it to a string
    json_string = json.dumps(res, indent=4)
    res_info = json.loads(json_string)

    # Checks if the API has returned a match and prints the info if true
    # or tries to find a match if false
    if (res_info["Response"] == "False"):
      print('Searching...')
      FindSomethingRandom()
    print("________________________________")
    print("Title: ", res_info["Title"])
    print(" - Year: ", res_info["Year"])
    print(" - Cast: ", res_info["Actors"])
    print(" - Plot: ", res_info["Plot"])
    print(" - Metascore: ", res_info["Metascore"])
    print("________________________________")

# Match/Case unaccepted in current python version and is not backwards compatible
# Elif statements used to ensure compliance with other editors
class App:
  while True:
    print("What would you like to do?")
    option = input("1 - Search for a movie | 2 - Get a random recommendation | 3 - Exit: ")

    if (option == '1'):
      while (True):
        query = input("Enter a movie title: ")
        search = MovieSearch(query)
        userSelect = input("Would you like to search for another movie? - Y|N: ")
        if (userSelect.upper() == "Y"):
          continue
        elif (userSelect.upper() == "N"):
          break
        else:
          print("No valid option selected")
          break
    elif (option == "2"):
      randomMovie = FindSomethingRandom()
    elif (option == "3"): 
      print("Oh ok... Bye then")
      break
    else:
      print("No valid option selected - Please try again")
