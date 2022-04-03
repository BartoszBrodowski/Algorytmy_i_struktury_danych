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
    print(arr)
    return small_el_index + 1

def quick_sort(arr, lowest, highest):
    # Sprawdzenie, czy indeksy na siebie nie nachodzą, czyli
    # czy lista jeszcze wymaga iteracji
    if lowest < highest:

        # partition_index to indeks elementu, wokół którego wykonano sortowanie, więc
        # jest on już ustawiony na odpowiednim miejscu w liście
        partition_index = partition(arr, lowest, highest)

        quick_sort(arr, lowest, partition_index - 1)
        quick_sort(arr, partition_index + 1, highest)

    return arr

tablica = [6,5,1,15,12,4]

print(quick_sort(tablica, 0, len(tablica) - 1))