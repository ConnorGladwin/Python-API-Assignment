import requests
import json

# TODO: List actors in movie

headers = {
  'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
  'x-rapidapi-key': "7b275e1179mshfbad81cf1295a2bp18c11bjsn8a05e938a08d"
}

# Searches for movie titles that match the user input name
class MovieSearch:
  def __init__(self, query):
    super().__init__()
    self.url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    # Query parameters
    self.query = {"s": query, "page": "1", "r": "json"}
    # API response
    res = requests.request("GET", self.url, headers=headers, params=self.query).json()
    # Parses the dict returned from the API and transforms it to a string
    json_string = json.dumps(res, indent=4)
    res_info = json.loads(json_string)
    # Prints the title to the console
    for movieTitle in res_info['Search']:
      print('________________')
      print(movieTitle['Title'])
      print(movieTitle['Year'])

# Find out where the movies can be watched
class WhereToWatch:
  def __init__(self):
    super().__init__()

# Find a random movie
class FindSomethingRandom:
  def __init__(self):
    super().__init__()

# Wiki listing for the movie
class MovieInfo:
  def __init__(self):
    super().__init__()


class App:
  while True:
    print('What would you like to do?')
    option = input('1 - Search for a movie | 2 - Get a random recommendation | 3 - Exit: ')

    if option == '1':
      while (True):
        query = input("Enter a movie title: ")
        search = MovieSearch(query)
        userSelect = input('Would you like to search for another movie? - Y|N: ')
        if userSelect.upper() == 'Y':
          continue
        elif userSelect.upper() == 'N':
          break
        else:
          print('boop')
    elif option == '2':
      randomMovie = FindSomethingRandom()
    elif option == '3': 
      print('Oh ok... Bye then')
      break
    else:
      print('No valid option selected - Please try again')