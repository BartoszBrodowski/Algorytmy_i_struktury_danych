from asyncio.windows_events import NULL
import fileinput

# Czytanie elementów z pliku tekstowego i wprowadzanie ich jako listy list
tablica_elementow = [line.replace('\n', '').split(' ') for line in fileinput.input(files='LinkedList/nazwiska.txt')]

# Zamiana stringów liczb na inty
for element in range(len(tablica_elementow)):
    tablica_elementow[element][0] = int(tablica_elementow[element][0])

# Tworzenie pustej tablicy hashy
hash_tablica = []
for i in range(2380):
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


def hashowanieLiniowe(tablica_hashy, nazwisko):
    m = len(tablica_hashy)
    for i in range(m):
        # TODO Wybiera nazwisko, trzbea dodać fora, żeby nie skipowało nazwisko, jeśli element jest zapełniony
        temp = (h1(ascii_nazwiska(tablica_elementow[i][1])) + i) % m
        wstawianie(tablica_hashy, temp, tablica_elementow[i][1])

def wstawianie(tablica_hashy, hash_nazwiska, element_do_wstawienia):
    if tablica_hashy[hash_nazwiska] == None:
        tablica_hashy[hash_nazwiska] = element_do_wstawienia
    # else: 


def main():
    pass