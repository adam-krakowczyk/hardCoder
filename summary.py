# #SUMMARY
# Napisz program, który odczytuje wszystkie pliki stworzone przez Ciebie podczas
# feriechallenge - przeszukuje lokalne katalogi lub łączy się w tym celu z Githubem.
# Postaraj się jak najmniej hardcodować i na przykład nie podawaj listy wszystkich plików ręcznie
# Następnie wykorzystując swój sposób katalogowania programów automat odczytuje
# i wyświetla takie informacje:
# - do ilu zadań z 10 napisało się kod
# - liczba linijek kodu napisanych w każdym zadaniu (bez uwzględniania pustych!)
#     oraz sumaryczna liczba linijek
# - liczba unikalnych słów użytych we wszystkich programach oraz najczęściej występujące słowo
# - lista i liczba słów kluczowych użyta podczas całego challenge (wykorzystaj moduł keywords)
# - lista i liczba zaimportowanych modułów we wszystkich programach
#     Propozycja rozszerzenia: Po prostu miej odwagę i pochwal się outputem swojego programu!
#     - opublikuj posta z tagiem #feriechallenge i zostaw lajka na naszej stronie,
#     będzie nam miło 🙂 Możesz też oczywiście umieścić jakieś dodatkowe statystyki.
from os import listdir
from os.path import isfile, join
import keyword

global_content = []


def filtered_code(content):
    filtered = []
    for line in content:
        if str(line).startswith('#'):
            continue
        if len(line) < 2:
            continue
        else:
            filtered.append(line.strip())
    return filtered


def word_count(content):
    wordsAndCount = {}
    
    for line in content:
        words_list = str(line).split()
        for word in words_list:
            wordd = word.strip("[](),.+-//='")
            if wordd.isalpha():
                try:
                  wordsAndCount[wordd] += 1
                except KeyError:
                    wordsAndCount[wordd] = 1
            else:
                continue
    return wordsAndCount


def key_word_count(content):
    keyWordsCount = {}
    
    for line in content:
        words_list = str(line).split()
        for word in words_list:
            wordd = word.strip("[](),.+-=//'")
            if keyword.iskeyword(wordd):
                    try:
                        keyWordsCount[wordd] += 1
                    except KeyError:
                        keyWordsCount[wordd] = 1
            else:
                continue

    return keyWordsCount

def imported_modules(content):
    importedModules={}
    for lines in content:
        for line in lines:
            if str(line).startswith('import'):
                word = line[7:]
                try:
                    importedModules[word] += 1
                except KeyError:
                    importedModules[word] = 1
            if str(line).startswith('from'):
                word = line[5:str(line).index('import')-1]
                try:
                    importedModules[word] += 1
                except KeyError:
                    importedModules[word] = 1
            else:
                continue
    return importedModules
    
baseDir = 'C:\\Projects\\Python\\HardCode\\scripts\\'
onlyfiles = [f for f in listdir(baseDir) if isfile(join(baseDir, f)) if f.upper().endswith('.PY')]
i = 0
summaryLine = 0
summaryLineCode = 0

for file in onlyfiles:
    i += 1
    print('\n', '-'*10, i, file, '-'*10)
    with open(baseDir+file, "r") as file:
        content = file.readlines()
        summaryLine += len(content)
        print(len(content), ': number of lines')
        filtered = filtered_code(content)
        summaryLineCode += len(filtered)
        print(len(filtered), ': number of code lines', '\n', '-'*40)
        global_content.append(filtered)
     
words = word_count(global_content)
modules = imported_modules(global_content)
inverse = {value: key for key, value in words.items()}

print('imported modules:', modules)
print ('keywords: ',key_word_count(global_content))
print('-'*10)
print('summary lines = ', summaryLine)
print('summary lines code = ', summaryLineCode)
print('Unique words in file: ', len(words))
print('max counted word: ', inverse[max(inverse.keys())],'-',max(inverse.keys()))
print('Imports count:', words['import'])
