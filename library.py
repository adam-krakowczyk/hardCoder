# HOUSE #LIBRARY
'''
Napisz program, który importuje katalog z dowolnej biblioteki
(np. API Biblioteki Narodowej http://data.bn.org.pl
przykład użycia: http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&ampkind=ksi%C4%85%C5%BCka)
Użytkownik może podać autora i program pokaże mu, jakie książki tego autora są w zbiorach biblioteki.
Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek -
posiadane pozycje są składowane w pliku zawierającym pewien identyfikujący zbiór danych,
np. tytuł, autor, wydawnictwo, rok wydania(możesz też użyć lokalnej bazy danych),
w przypadku “wypożyczenia” książki są do niego dodawane, a w przypadku “zwracania” usuwane.
Propozycja rozszerzenia:
W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki,
czyli w teorii można wypożyczyć książkę nieskończoną liczbę razy.
Zabezpiecz program w taki sposób, aby podczas pobierania danych
rozpoznawał też pozycje “wypożyczone” lokalnie i nie pokazywał ich już jako wyniki wyszukiwania.
'''

import requests
import sqlite3
from os import system


def create_data_base(base_name):
    '''
    Run only once!
    '''
    with sqlite3.connect(base_name+'.db') as conn:
        conn.cursor().execute("""CREATE TABLE books (
                            id int,
                            author text,
                            title text,
                            publication_year text,
                            publisher text
                            )""")


class Book:
    ''' book
    '''

    def __init__(self, id, author, title, year, publisher):
        self.id = id
        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher

    def __str__(self):
        return 'id: ' + str(self.id) + ' Title: ' + self.title + '\nAuthor: ' + self.author + '\nPublished: ' + self.year + ' by ' + self.publisher + '\n'

    def db_insert_book(self):
        query = ''' INSERT INTO books (
                        id,
                        author,
                        title,
                        publication_year,
                        publisher)
                        VALUES (
                        ?,?,?,?,?) '''
        inserts = [self.id, self.author, self.title, self.year, self.publisher]
        with sqlite3.connect('localLibrary.db') as conn:
            conn.cursor().execute(query, inserts)

            # conn.commit()
            print('Enjoy reading \n')


class Books:

    def __init__(self):
        self._books = []

    def __str__(self):

        def cls(): return system('cls')
        print('Booki:')
        booksList = ''
        i = 0
        for book in self._books:
            i += 1
            booksList += str(i) + ' - ' + ''.join(str(book))
        return booksList

    def list_books(self):

        system('cls')
        print('List of books:')
        booksList = ''
        i = 0
        for book in self._books:
            i += 1
            booksList += str(i) + ' - ' + ''.join(str(book))
        print(booksList)
        choice = input(('Type books number [x] to borow or [q] to quit: '))
        if choice != 'q':
            book_to_db = self._books[int(choice)-1]
            book_to_db.db_insert_book()
        else:
            return

    def get_author_books(self, author):

        url = 'https://data.bn.org.pl/api/bibs.json'
        querystring = {"author": author, "kind": "książka", 'limit': "5"}
        response = requests.request("GET", url, params=querystring)
        bookslist = response.json()['bibs']

        for item in bookslist:
            book = Book(item['id'], item['author'], item['title'],
                        item['publicationYear'], item['publisher'])
            self._books.append(book)
        self.list_books()


def show_books_in_db():
    query = ''' select * from books '''
    records = []
    i = 0
    with sqlite3.connect('localLibrary.db') as conn:
        records = conn.cursor().execute(query).fetchall()
        print('\n----- List of borowed books ----------\n')
        for record in records:
            i += 1
            print(f'{record}')
        choice = (input('\nType Id to return book, or (q) to quit : '))
        return choice


def remove_book_in_db(id):
    query = f''' delete  from books where id ={id} '''
    with sqlite3.connect('localLibrary.db') as conn:
        records = conn.cursor().execute(query)
    print('Thx for return book ', id)


# create_data_base('localLibrary')
localLibrary = Books()

choice = ''
while choice != 'q':
    system('cls')
    print('[1] show author books \n[2] Return Book\n[q] End\n')
    choice = input('\nPleas choice: ')

    if choice == '1':
        localLibrary.get_author_books(input('\nPleas type author name: '))
        localLibrary.list_books()

    elif choice == '2':
        book_id = show_books_in_db()
        if book_id == 'q':
            continue
        else:
            remove_book_in_db(book_id)

    else:
        break
