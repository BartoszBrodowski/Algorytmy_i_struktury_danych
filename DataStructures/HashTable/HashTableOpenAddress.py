import fileinput

ilosc_wstawien_global = 0
ilosc_udanych_wstawien = 0
# Czytanie elementów z pliku tekstowego i wprowadzanie ich jako listy list
tablica_elementow = [line.replace('\n', '').split(
    ' ') for line in fileinput.input(files='nazwiska199.txt')]

# Zamiana stringów liczb na inty
for element in range(len(tablica_elementow)):
    tablica_elementow[element][0] = int(tablica_elementow[element][0])

# Tworzenie pustej tablicy hashy
hash_tablica = []
for i in range(len(tablica_elementow)):
    hash_tablica.append(None)


def ascii_nazwiska(klucz):
    wynik = 0
    for i in klucz:
        wynik += ord(i)
    return wynik


def h1(klucz):
    return klucz % len(hash_tablica)


def h2(klucz):
    return 1 + (klucz % (len(hash_tablica) - 2))


def wywołanieHashowania(typ_hashowania, procenty):
    m = len(hash_tablica)
    if typ_hashowania == "Liniowe" or typ_hashowania == "liniowe":
        for i in range(m):
            if ilosc_udanych_wstawien < int(m*procenty):
                wstawianieLiniowe(
                    hash_tablica, tablica_elementow[i][1])
    if typ_hashowania == "Kwadratowe" or typ_hashowania == "kwadratowe":
        for i in range(m):
            if ilosc_udanych_wstawien < int(m*procenty):
                wstawianieKwadratowe(
                    hash_tablica, tablica_elementow[i][1])
    if typ_hashowania == "Dwukrotne" or typ_hashowania == "dwukrotne":
        for i in range(m):
            if ilosc_udanych_wstawien < int(m*procenty):
                wstawianieDwukrotne(
                    hash_tablica, tablica_elementow[i][1])
    else:
        return


def wstawianieLiniowe(tablica_hashy, element_do_wstawienia):
    m = len(tablica_hashy)
    for j in range(m):
        global ilosc_wstawien_global
        global ilosc_udanych_wstawien
        ilosc_wstawien_global += 1
        temp = (h1(ascii_nazwiska(element_do_wstawienia)) + j) % m
        if tablica_hashy[temp] == None:
            tablica_hashy[temp] = element_do_wstawienia
            ilosc_udanych_wstawien += 1
            break
        # else:
        #     if tablica_hashy[temp] != None and j == len(tablica_hashy):
        #         return


def wstawianieKwadratowe(tablica_hashy, element_do_wstawienia):
    m = len(tablica_hashy)
    for j in range(m):
        global ilosc_wstawien_global
        global ilosc_udanych_wstawien
        ilosc_wstawien_global += 1
        temp = (h1(ascii_nazwiska(element_do_wstawienia)) + j*j) % m
        if tablica_hashy[temp] == None:
            tablica_hashy[temp] = element_do_wstawienia
            ilosc_udanych_wstawien += 1
            break


def wstawianieDwukrotne(tablica_hashy, element_do_wstawienia):
    m = len(tablica_hashy)
    for j in range(m):
        global ilosc_wstawien_global
        global ilosc_udanych_wstawien
        ilosc_wstawien_global += 1
        temp = (h1(ascii_nazwiska(element_do_wstawienia)) + j *
                h2(ascii_nazwiska(element_do_wstawienia))) % m
        if tablica_hashy[temp] == None:
            tablica_hashy[temp] = element_do_wstawienia
            ilosc_udanych_wstawien += 1

            break


def main():
    wywołanieHashowania("Liniowe", 0.5)
    # print(hash_tablica)
    print(hash_tablica)
    print(len(hash_tablica))

    # Funkcja do sprawdzenia ilości operacji, nie jest podane w
    # treści zadania, więc nie uwzględniam w pomiarze
    # print(ilosc_wstawien_global)

    print(ilosc_wstawien_global/ilosc_udanych_wstawien)
    print(ilosc_udanych_wstawien)


main()

### testy na małej tablicy m=199 ###
# używamy pliku nazwiska200.txt

# W+OL 50%: 1.46, 70%: 1.94, 90%: 3.05

# W+OK 50%: 1.41, 70%: 1.93, 90%: 2.62

# W+OD 50%: 1.50, 70%: 1.92, 90%: 2.40


##########################################


### średnia ilość prób dla m=2503 ###
# W+OL 50%: 231.52, 70%: 455.52, 90%: 682.79

# W+OK 50%: 11.54, 70%: 17.4, 90%: 22.19

# W+OD 50%: 2.73, 70%: 3.89, 90%: 6.43

# Dwukrotne 0.9 m=199
# ['Bednarek', 'Majchrzak', 'Kubiak', None, 'Przybylski', 'Szulc', 'Brzozowski', 'Nawrocki', 'Janicki', 'Wilk', 'Krol', 'Pawlak', 'Tomczak', 'Mroz', None, 'Kruk', 'Bielecki', 'Urbaniak', 'Wojcik', 'Pawlik', 'Sikora', 'Glowacki', 'Wrobel', 'Kot', 'Adamczyk', 'Gajewski', 'Gorski', 'Kaminski', None, 'Sowa', 'Mazurek', 'Majewski', 'Jasinski', 'Czerwinski', 'Ciesielski', 'Urbanski', 'Jarosz', 'Dziedzic', 'Klimek', 'Lipinski', 'Stefanski', 'Kowalski', 'Sadowski', 'Kasprzak', None, 'Sliwinski', 'Jaworski', 'Matuszewski', 'Sobczak', 'Luczak', 'Mikolajczyk', 'Sikorski', 'Borowski', 'Czajka', 'Markowski', 'Jakubowski', None, 'Kalinowski', 'Krawczyk', 'Malinowski', 'Romanowski', 'Domanski', 'Kowalewski', None, 'Wasilewski', 'Kowal', 'Wawrzyniak', 'Jozwiak', 'Jablonski', 'Zakrzewski', 'Wroblewski', 'Bak', 'Brzezinski', 'Kozak', 'Wisniewski', 'Baranowski', 'Orlowski', 'Koziol', 'Szewczyk', 'Wolski', 'Musial', 'Maj', 'Sokolowski', 'Kazmierczak', 'Kucharski', None, 'Baran', 'Skiba', 'Piotrowski', 'Piatek', 'Zieba', 'Zajac', 'Milewski', 'Makowski', None, 'Dudek', 'Krajewski', 'Lis', 'Marek', 'Mucha', 'Kopec', 'Pietrzak', 'Socha',
#     'Cieslak', None, 'Polak', 'Urban', 'Wierzbicki', 'Gajda', 'Kania', 'Chojnacki', 'Gorecki', 'Jastrzebski', 'Markiewicz', 'Nowak', 'Marciniak', 'Kurek', 'Krupa', 'Sawicki', 'Nowacki', 'Walczak', 'Michalski', 'Laskowski', 'Kowalik', 'Malecki', 'Kaczmarek', 'Czarnecki', 'Nowicki', 'Borkowski', 'Mazur', 'Sosnowski', 'Stepien', 'Szczepaniak', 'Czajkowski', None, 'Adamski', None, 'Maciejewski', 'Dabrowski', 'Tomczyk', 'Pawlowski', 'Grabowski', 'Wozniak', 'Kolodziej', 'Karpinski', 'Piasecki', 'Chmielewski', 'Ratajczak', 'Wysocki', 'Jankowski', 'Zielinski', 'Wieczorek', 'Wilczynski', 'Wlodarczyk', None, 'Andrzejewski', 'Zalewski', 'Szymczak', None, 'Nowakowski', 'Olszewski', 'Blaszczyk', None, 'Kowalczyk', None, 'Lewandowski', 'Ziolkowski', 'Kaczmarczyk', 'Grzelak', 'Stankiewicz', 'Duda', 'Madej', 'Dobrowolski', 'Szymanski', 'Bednarczyk', 'Wojciechowski', 'Witkowski', 'Kozlowski', 'Szczepanski', 'Wesolowski', 'Wojtowicz', 'Kwiatkowski', None, 'Rutkowski', 'Stasiak', 'Ostrowski', None, None, None, 'Olejniczak', 'Tomaszewski', 'Zawadzki', None, 'Zak', 'Kolodziejczyk', 'Janik', 'Domagala', 'Michalak', 'Leszczynski']


# Liniowe 0.5 m=199
# [None, None, 'Kubiak', None, None, None, None, None, None, 'Wilk', 'Krol', 'Pawlak', None, None, None, None, None, None, 'Wojcik', None, 'Sikora', 'Glowacki', 'Wrobel', None, 'Adamczyk', 'Gajewski', 'Gorski', 'Kaminski', 'Domanski', None, None, 'Majewski', 'Jasinski', None, None, 'Urbanski', None, None, None, None, None, 'Kowalski', 'Zawadzki', 'Sadowski', 'Makowski', None, 'Jaworski', 'Pietrzak', 'Zalewski', 'Baranowski', None, 'Sikorski', 'Borowski', None, None, 'Jakubowski', None, 'Kalinowski', 'Krawczyk', 'Malinowski', None, None, None, None, 'Wasilewski', 'Szymczak', None, None, None, None, 'Wroblewski', 'Bak', 'Wlodarczyk', 'Czerwinski', 'Wisniewski', 'Nowakowski', 'Andrzejewski', 'Brzezinski', 'Szewczyk', None, None, None, 'Sokolowski', 'Zakrzewski', 'Ziolkowski', None, 'Baran', None, 'Piotrowski', None, None, 'Zajac', None, None, None, 'Dudek', 'Przybylski', 'Lis', None, None, None,
#     'Adamski', None, 'Cieslak', None, None, None, None, None, None, 'Chojnacki', None, None, None, 'Nowak', 'Marciniak', None, None, 'Sawicki', 'Nowacki', 'Walczak', 'Michalski', 'Sobczak', None, None, 'Kaczmarek', 'Czarnecki', 'Nowicki', None, 'Mazur', 'Jablonski', 'Stepien', 'Szulc', None, None, None, None, 'Maciejewski', 'Dabrowski', 'Kucharski', 'Mazurek', 'Grabowski', 'Wozniak', 'Kolodziej', 'Krajewski', None, 'Chmielewski', None, 'Wysocki', 'Jankowski', 'Zielinski', 'Wieczorek', None, 'Kazmierczak', None, None, 'Laskowski', None, None, 'Borkowski', None, 'Blaszczyk', None, 'Kowalczyk', None, 'Lewandowski', 'Pawlowski', None, None, None, None, None, None, 'Szymanski', None, 'Wojciechowski', 'Olszewski', 'Kozlowski', 'Witkowski', 'Szczepanski', None, 'Kwiatkowski', None, 'Rutkowski', 'Duda', 'Ostrowski', None, None, None, None, 'Tomaszewski', None, None, None, None, None, None, 'Michalak', None]
