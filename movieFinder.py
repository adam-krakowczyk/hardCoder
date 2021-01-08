# MOVIE #FINDER
# Przy wykorzystaniu API (np. IMDB) wyszukaj wszystkie części filmu zadanego w wyszukiwaniu
# (np. Rambo, Scary Movie, Shrek). Można przyjąć założenie,
# że wszystkie filmy “z serii” muszą zawierać szukany ciąg -
# czasem zdarzają się błędne wyniki wyszukiwania z baz,
# można je spróbować odfiltrować. Wyświetl dla każdego podstawowe informacje
# np. rok, długość, ocena, spis aktorów (pierwszych 5 z listy).
# Przykładowe API do wykorzystania:
# https://rapidapi.com/apidojo/api/imdb8/endpoints - do wyszukania filmów z daną nazwą
# (do odfiltrowania można użyć warunku, że dany rekord posiada nazwę i rok wydania)
# https://rapidapi.com/.../imdb-internet-movie-database... - pobranie szczegółów o danym filmie

import requests

def searchFilm(searchTitle):
    filmIds=[]
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = {"q":searchTitle}
    headers = {
        'x-rapidapi-key': "7ad25462ecmshfc519d0047cbca9p1ea5f5jsnc13500c50fef",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
            }
    response = requests.request("GET", url, headers=headers, params=querystring)
    filmList = response.json()["d"]
    for item in filmList:
        filmIds.append(item['id'])
    return filmIds


def filmInfo(filmIds):


    headers = {
        'x-rapidapi-key': "7ad25462ecmshfc519d0047cbca9p1ea5f5jsnc13500c50fef",
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
            }

    for filmId in filmIds:
        url = f'https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{filmId}'
        response = requests.request("GET", url, headers=headers)
        filmDetails = response.json()
        if len(filmDetails['title'])>0 and len(filmDetails['year'])>0:
            print('Title: ',filmDetails['title'],'Year:',filmDetails['year'], 'Rating: ',filmDetails['rating'])
            print('---------Cast----------')
            for i in range(5):
                try:
                    print(filmDetails['cast'][i]['actor'], '-', filmDetails['cast'][i]['character'])
                except IndexError:
                    break
            print ('-'*5)


filmInfo(searchFilm(input('Podaj tytuł szukanego filmu: ')))

