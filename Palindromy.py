'''
@krakaman

polindromy
'''
import webbrowser

def reversWords (words):
    wordCheck= ''.join([char for char in words if char.isalpha()])
    reverseCheck = wordCheck[-1::-1].lower().replace(' ','')
    reverse = words[-1::-1]
    print ("to jest polindrom" if reverseCheck==wordCheck.lower().replace(' ', '') else "słowa nie są palindromem" )
    print (reverse)             # to słowo wspak bez usuwania zbędnych znaków

    website = "https://poocoo.pl/scrabble-slowa-z-liter/" + wordCheck
    webbrowser.open(website)


reversWords(input ("Podaj dowolny napis: "))