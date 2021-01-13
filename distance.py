# #DISTANCE #CALCULATOR
# Napisz program liczący odległość liniową między dwoma dowolnymi punktami na mapie,
# wykorzystujący ich współrzędne geograficzne (długość i szerokość geograficzną).
# Wykorzystaj dowolny algorytm, np. https://pl.wikibooks.org/.../Astrono.../Odleg%C5%82o%C5%9Bci
# Skorzystaj z API (np. https://rapidapi.com/trueway/api/trueway-geocoding),
# żeby obliczyć odległość pomiędzy twoim adresem, a charakterystycznymi punktami np. Wieżą Eiffla czy Tadź Mahal.
# Propozycja rozszerzenia: zamiast podawać swój adres, użyj geolokalizacji

from math import sin, cos, sqrt, asin, radians
import requests


def distance(A, B):
    earthRadius = 6371
    diffLat = radians(B['lat']) - radians(A['lat'])
    diffLong = radians(B['lng']) - radians(A['lng'])

    a = sin(diffLat/2)**2 + cos(radians(A['lat'])) * \
        cos(radians(B['lat'])) * sin(diffLong/2)**2
    c = 2 * asin(sqrt(a))
    dist = round((earthRadius*c), 2)
    return dist


def get_point(addres):

    url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
    queryString = {"address": addres}
    # print(querystring)
    headers = {
        'x-rapidapi-key': "your key",
        'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=queryString)
    # print(response.text)
    point = response.json()
    return point['results'][0]['location']


def getLocation():
    point = {}
    url = 'http://freegeoip.net/json'
    response = requests.request("GET", url)
    j = response.json()
    point['lat'] = j['latitude']
    point['lng'] = j['longitude']
    return point


addA = input('Type addres your location [city, street, country]: ')
A = get_point(addA)


destinations = ['Eiffel Tower, Paris',
                'Taj Mahal, India', 'Volgograd, kirov, Russia']
for addres in destinations:
    B = get_point(addres)
    print(
        f'Distance {addA} ({A["lat"]},{A["lng"]}) from {addres} - ({B["lat"]},{B["lng"]})')
    print(distance(A, B), 'km')
