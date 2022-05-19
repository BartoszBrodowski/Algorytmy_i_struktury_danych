# Tablica m = 17
with open('HashTable\slowa.txt') as file:
    tablica17 = [next(file).strip('\n') for line in range(2*17)]

# Tablica m = 1031
with open('HashTable\slowa.txt') as file:
    tablica1031 = [next(file).strip('\n') for line in range(2*1031)]

# Tablica m = 1024
with open('HashTable\slowa.txt') as file:
    tablica1024 = [next(file).strip('\n') for line in range(2*1024)]

pusta_tablica17 = [[] for element in range(17)]
pusta_tablica1031 = [[] for element in range(1031)]
pusta_tablica1024 = [[] for element in range(1024)]


# Wbudowana funkcja Hash
def W(tablicaW, pusta_tablicaW):
    for word in range(len(tablicaW)):
        pusta_tablicaW[hash(tablicaW[word]) % len(
            pusta_tablicaW)].append(hash(tablicaW[word]))

    return pusta_tablicaW


# funkcja D
def D(tablicaD, pusta_tablicaD):
    for klucz in range(len(tablicaD)):
        nowy_hash = 1
        for letter in range(len(tablicaD[klucz])):
            nowy_hash = nowy_hash * 111 + ord(tablicaD[klucz][letter])
        pusta_tablicaD[nowy_hash % len(pusta_tablicaD)].append(nowy_hash)

    return pusta_tablicaD


# Po pierwszej literze słowa
def S(tablicaS, pusta_tablicaS):
    for klucz in range(len(tablicaS)):
        nowy_hashS = ord(tablicaS[klucz][0])*111
        pusta_tablicaS[nowy_hashS % len(pusta_tablicaS)].append(nowy_hashS)

    return pusta_tablicaS


W(tablica1024, pusta_tablica1024)
print('\n')
# print(pusta_tablica17)


def Sprawdzanie_danych(pusta_tablica):
    puste_listy = 0
    średnia_długość = 0
    max_długość = 0
    for i in range(len(pusta_tablica)):
        if pusta_tablica[i] == []:
            puste_listy += 1
        if pusta_tablica[i] != []:
            średnia_długość += len(pusta_tablica[i])
        if len(pusta_tablica[i]) > max_długość:
            max_długość = len(pusta_tablica[i])

    print("Ilosc pustych list: " + str(puste_listy))
    print("Srednia dlugosc niepustych list: " +
          str(średnia_długość/(len(pusta_tablica) - puste_listy)))
    print("Maksymalna dlugosc listy: " + str(max_długość))


Sprawdzanie_danych(pusta_tablica1024)


######### WYNIKI ###########

# Lista m = 17, funkcja W

# Ilosc pustych list: ~2.6
# Srednia dlugosc niepustych list: ~2.516
# Maksymalna dlugosc listy: ~5

# Lista m = 17, funkcja D

# Ilosc pustych list: 2
# Srednia dlugosc niepustych list: 2.26(6)
# Maksymalna dlugosc listy: 4

# Lista m = 17, funkcja S

# Ilosc pustych list: 2
# Srednia dlugosc niepustych list: 2.26(6)
# Maksymalna dlugosc listy: 5


# Lista m = 1031, funkcja W

# Ilosc pustych list: ~139.8
# Srednia dlugosc niepustych list: ~2.308
# Maksymalna dlugosc listy: ~7.6

# Lista m = 1031, funkcja D

# Ilosc pustych list: 117
# Srednia dlugosc niepustych list: 2.2560175054704596
# Maksymalna dlugosc listy: 8

# Lista m = 1031, funkcja S

# Ilosc pustych list: 981
# Srednia dlugosc niepustych list: 41.24
# Maksymalna dlugosc listy: 183


# Lista m = 1024, funkcja W

# Ilosc pustych list: ~144
# Srednia dlugosc niepustych list: ~2.32
# Maksymalna dlugosc listy: ~8.6

# Lista m = 1024, funkcja D

# Ilosc pustych list: 144
# Srednia dlugosc niepustych list: 2.327272727272727
# Maksymalna dlugosc listy: 8

# Lista m = 1024, funkcja S

# Ilosc pustych list: 974
# Srednia dlugosc niepustych list: 40.96
# Maksymalna dlugosc listy: 183


#### ODPOWIEDZI ####
# W i D Lepszy wynik wychodzi dla m=1031, S wychodzi lepszy wynik dla m=1024, różnice są nieznaczne

# Wybór rodzaju funkcji mocno wpływa na jakość wyniku, widać to, gdy porównujemy funkcje W/D z S.
# Różnice pomiędzy W a D są nieznaczne, lecz funkcja W powoduje różne wyniki przy każdym
# wywołaniu funkcji.
