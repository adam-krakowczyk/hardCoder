# Napisz program, który na podstawie masy [kg] i wzrostu [cm] wylicza wskaźnik BMI
# (https://en.wikipedia.org/wiki/Body_mass_index)
# oraz informuje użytkownika, w jakim jest zakresie.
# Zakresy można wpisać “z palca”
# Następnie program losuje jedną z aktywności fizycznych oraz czas jej wykonania,
# np. bieganie przez 30 minut.
# Czas nie może być dłuższy niż podany przez użytkownika
# (maksymalny czas, który można poświęcić na ćwiczenia).
# Zadbaj o to, aby czas aktywności był jakoś uzależniony od BMI
# (na przykład osoba z niedowagą nie powinna ćwiczyć mniej niż osoba o wadze normalnej
# - ustal pewien minimalny czas; ale już osoba z nadwagą powinna ćwiczyć dłużej
# -ustal odpowiedni nieliniowy mnożnik, tak aby nie przekroczyć maksimum).
# Utwórz w ten sposób plan treningowy na 7 następnych dni, wyniki zapisując do pliku .txt.

import random

def bmi_calc(mass,height):
    bmi = mass / ((height/100) ** 2)

    if bmi <= 16.99:
        category = 'wychudzenie'

    elif bmi >= 17 and bmi <= 18.49:
        category = 'niedowaga'

    elif bmi >= 18.5 and bmi <= 24.99:
        category = 'pożądana masa ciała'

    elif bmi >= 25 and bmi <= 29.99:
        category = 'nadwaga'

    elif bmi >= 30 and bmi <= 34.99:
        category = 'otyłość I stopnia'

    elif bmi >= 35 and bmi <= 39.99:
        category = 'otyłość II stopnia'
    else:
        category = 'otyłość III stopnia'
    print('-'*20)
    print(f'Twój wskaźnik BMI = {bmi:.2f}, kategoria - {category}')
    print('-'*20)
    return bmi


def get_activities(time,bmi):
    activities = ['biegania', 'tenis', 'koszykówka', 'pływanie', 'aerobik', 'spacer']
    sportDay =[]
    with open("plan_treningowy.txt", "w", encoding="UTF-8") as file:
        for day in range(1,8):
            doSport = random.choice(activities)
            sportTime = random.randint(int(bmi), time)
            print(f'Dzień {day} zalecana aktywność "{doSport}" przez conajmniej {sportTime} min.')
            file.write(f'Dzień {day} zalecana aktywność "{doSport}" przez conajmniej {sportTime} min.\n')
        file.close()


if __name__ == "__main__":
    mass = float(input('Podaj masę ciała w kg: '))
    height = float(input('Podja wzrost w cm: '))
    time = float(input('Ile czasu poświęcisz na aktywność w minutach: '))
    get_activities(time, bmi_calc(mass, height))