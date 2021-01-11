# # IMAGE #RESIZER
# Napisz program, który w wybranej lokalizacji odczyta wszystkie
# pliki graficzne
# (w określonych formatach, np. jpg, png, bmp itp.),
# następnie zmniejszy ich # rozdzielczość o 50 %
# i zapisze je w podkatalogu “smaller” z odpowiednimi nazwami.
# Wykorzystaj pillow lub inną bibliotekę do pracy z obrazami.
# Propozycja rozszerzenia:
# Oblicz ile miejsca na dysku można oszczędzić po kompresji
#  (odczytaj rozmiar plików w pierwotnym folderze oraz "smaller"
#   i porównaj obie wartości - bezwzględnie i w f


from PIL import Image
from os import listdir, stat
from os.path import isfile, join


baseDir = 'C:\\Projects\\Python\\HardCode\\scripts\\ImageResizer\\images'
destDir = 'C:\\Projects\\Python\\HardCode\\scripts\\ImageResizer\\smaller'


def image_resizer(path):
    basewidth = 300
    img = Image.open(f'{baseDir}\\{path}')
    hsize = int((float(img.size[1]) * float(0.5)))
    vsize = int((float(img.size[0]) * float(0.5)))

    #img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = img.resize((vsize, hsize), Image.ANTIALIAS)
    img.save(f'{destDir}\\{path}')


def imageCompression(path):
    return stat(path).st_size


onlyfiles = [f for f in listdir(baseDir) if isfile(join(baseDir, f)) if f.upper(
).endswith('.JPG') or f.upper().endswith('.PNG') or f.upper().endswith('.GIF')]


for image in onlyfiles:
    print(f'{image}')
    image_resizer(image)
    originalSize = imageCompression(f'{baseDir}\\{image}')
    compressedSize = imageCompression(f'{destDir}\\{image}')
    ratio = (compressedSize/originalSize) * 100
    print(
        f'rozmiar przed {originalSize} rozmiar po kompresji {compressedSize} ratio= {ratio:.2} %')
