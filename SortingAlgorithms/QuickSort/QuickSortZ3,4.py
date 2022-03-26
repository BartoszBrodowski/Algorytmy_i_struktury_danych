import sys
import threading
import random

sys.setrecursionlimit(100000)
threading.stack_size(100000)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def partition(arr, lowest, highest):
    # Zaczynamy od elementu najbardziej na lewo, ale quicksort może
    # zaczynać od dowolnego elementu
    pivot = arr[highest]

    # Indeks mniejszego elementu po całej iteracji
    # wyznacza miejsce, w które wstawia się pivot
    small_el_index = lowest - 1

    for j in range(lowest, highest):
        if arr[j] < pivot:
            small_el_index += 1
            arr[j], arr[small_el_index] = arr[small_el_index], arr[j]

    # Zamiana miejsc pivota z ostatnim mniejszym od pivota elementem,
    # czyli wstawienie go w odpowiednie miejsce w liście
    arr[highest], arr[small_el_index + 1] = arr[small_el_index + 1], arr[highest]

    # return potrzebny, do partition_index w quicksort
    # (pozwala iterować od lewej i prawej strony pivota)
    return small_el_index + 1


def sortowanie_szybkie(arr, lowest, highest):
    # Sprawdzenie, czy indeksy na siebie nie nachodzą, czyli
    # czy lista jeszcze wymaga iteracji
    if lowest < highest:
        # partition_index to indeks elementu, wokół którego wykonano sortowanie, więc
        # jest on już ustawiony na odpowiednim miejscu w liście

        # Na podstawie zmiennej c instrukcja warunkowa wybiera insertion/quick sort
        if len(arr) > c:
            partition_index = partition(arr, lowest, highest)
            sortowanie_szybkie(arr, lowest, partition_index - 1)
            sortowanie_szybkie(arr, partition_index + 1, highest)
        else:
            insertionSort(arr)
            # insertion_sort

    return arr


# tablica = [10, 80, 30, 90, 40, 50, 70]

tablica_losowa = []
for i in range(1000):
    tablica_losowa.append(random.randint(0, 100))
# print(tablica_losowa)

# print(sortowanie_szybkie(tablica, 0, len(tablica) - 1))

c = 0 # Stała do wprowadzenia
print(sortowanie_szybkie(tablica_losowa, 0, len(tablica_losowa) - 1))
# sortowanie = threading.Thread(target=sortowanie_szybkie(tablica_losowa, 0, len(tablica_losowa) - 1))
# sortowanie.start()
