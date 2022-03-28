import sys
import threading
import random
import time

tablica_losowa = []
for i in range(20000):
    tablica_losowa.append(random.randint(0, 100))

c = 30000

# 20.000 elementów = 33.07 sekund dla c = 30.000



# sys.setrecursionlimit(100000)
# threading.stack_size(100000)

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
    pivot = arr[highest - 1]

    # Indeks mniejszego elementu po całej iteracji
    # wyznacza miejsce, w które wstawia się pivot
    small_el_index = lowest - 1

    for j in range(lowest, highest):
        if arr[j] < pivot:
            small_el_index += 1
            arr[j], arr[small_el_index] = arr[small_el_index], arr[j]

    # Zamiana miejsc pivota z ostatnim mniejszym od pivota elementem,
    # czyli wstawienie go w odpowiednie miejsce w liście
    arr[highest - 1], arr[small_el_index + 1] = arr[small_el_index + 1], arr[highest - 1]

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

# sortowanie = threading.Thread(target=sortowanie_szybkie(tablica_losowa, 0, len(tablica_losowa) - 1))
# sortowanie.start()

start_time = time.process_time()

sortowanie_szybkie(tablica_losowa, 0, len(tablica_losowa))


print(" --- %s seconds --- " % (time.process_time()))