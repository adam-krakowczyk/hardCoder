# Stwórz prosty program, który będzie wysyłał spersonalizowany mailing do wybranych osób.
# “Bazą danych” jest plik Excela lub CSV, zawierający dwie kolumny z nagłówkami:
# “E-mail” oraz “Imię i nazwisko” (zakładamy, że zawsze w takiej kolejności, a imię i nazwisko są oddzielone spacją).
# Do użytkowników należy wysłać maila z tematem “Your image” oraz spersonalizowaną prostą treścią np.
# “Hi {Imię}! it’s file generated for you”.
# Dodatkowo w załączniku maila znajduje się plik graficzny o nazwie “{Imię}_{Nazwisko}_image.png” (pliki są w zadanej lokalizacji).
# Odpowiednio zabezpiecz program (np. brakujący plik Excela, brakujące dane w Excelu, brak pliku png)
# oraz zabezpiecz przed spamowaniem (np. jeden mail wysyłany co 1 sekundę).
# Mogą przydać się moduły: smtplib, email, ssl, xlrd, re, os.
#
# Propozycje rozszerzenia: dodaj opcję wysyłania maili z treścią w HTML oraz walidator poprawności maila
# (np. używając wyrażeń regularnych - moduł re).


import smtplib
# import email
import ssl
import yagmail
import xlrd
import re
import os
from os.path import isfile
import time
errorLog = {}
errorCount = 0


def read_excel(path) -> list:
    """
    Open and read an Excel file
    """
    global errorLog
    global errorCount
    if not isfile(path):
        print('File doesnt exist: ', path)
        return

    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_index(0)
    i = 1
    correct = 0
    badData = 0
    mailing = []
    while i <=first_sheet.nrows-1:
          if len(first_sheet.row_values(i)[1])>0 and first_sheet.row_values(i)[1].index(' ')>0 and len(first_sheet.row_values(i)[0])>0:
              name = first_sheet.row_values(i)[1].split()
              firstName = name[0]
              lastName = name[1]
              email = first_sheet.row_values(i)[0]
              mailing.append([firstName, lastName, email])
              correct+=1
              print('[+]',i, first_sheet.row_values(i))
          else:
              print ('[-]',i, first_sheet.row_values(i))
              errorCount += 1
              badData+=1
              errorLog[errorCount] = [f'[-] ExcelProcess', first_sheet.row_values(i)]
          i+=1
    print('odczytano poprawnie: ', correct ,' adresatów, oraz', badData,' nieporawnie')
    return mailing


# ----------------------------------------------------------------------
def send_mail(mailList):
    '''
    send mail to person in list
    :param mailist: ['firstname','lastname', 'email address']
    :return:
    '''
    global errorLog
    global errorCount
    i = 1
    error = 0
    if mailList == []:
        return 'brak listy do wyslania'
    else:
        EMAIL_ADDRESS = "mail@gmail.com"
        EMAIL_PASSWORD = 'pass'
        imagesPath = "C:\\Projects\\Python\\HardCode\images\\"

        for person in mailList:
            receiver = person[2]
            filename = f'{imagesPath}{person[0]}_{person[1]}_image.png'
            body = f'Hi {person[0]}! it’s file generated for you'
            contents = [body, r'%s' % filename]

            if os.path.isfile(filename):
                print(f'[+] {i} {receiver}')
                yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
                yag.send(to=receiver,
                         subject="Your image",
                         contents=contents
                         )
                i += 1
                time.sleep(1)
            else:
                print(f'[-] {i} {receiver} plik {filename} nie istnieje ')
                errorLog[errorCount] = [f'FileError, plik = {filename}']
                errorCount+=1
                error += 1
                i += 1


    return f'wysłano {i-error} maile z {len(mailList)}'


# -----------------------------------------------
if __name__ == "__main__":
    print('--Excel proces--')
    mailList = read_excel(path)
    print ('--Wysyłaka--')
    print(send_mail(mailList))
    print ('--Error Log--')
    print(errorLog)