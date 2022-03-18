def heapify(array, array_length, root_node_index):                                  # Tablica, długość tablicy, indeks rodzica

    biggest_value_index = root_node_index                                           # Definiuję największą wartość poddrzewa jako ideks rodzica (nie wiadomo czy jest największa, ale taka powinna być)
    left_child = root_node_index * 2 + 1                                            # Lewe dziecko w poddrzewie
    right_child = root_node_index * 2 + 2                                           # Prawe dziecko w poddrzewie

    if left_child < array_length and array[left_child] > array[biggest_value_index]: # Sprawdzam czy istnieje lewe dziecko, następnie sprawdzam czy lewe dziecko jest większe od rodzica
        biggest_value_index = left_child                                             # Nie array[left_child], bo wtedy przypisuję wartość a nie indeks
                                                                                     # co powoduje problem przy rekurencji oraz swapowaniu w 3 if'

    if right_child < array_length and array[right_child] > array[biggest_value_index]: # Sprawdzam czy istnieje prawe dziecko, następnei sprawdzam czy prawe dziecko jest większe od rodzica
        biggest_value_index = right_child

    if root_node_index != biggest_value_index:                                         # Jeśli rodzic nie ma największej wartości to zamieniam go z elementem o największej wartości
                                                                                       # (zamieniam wartości dla konkretnych indeksów a nie indeksy)

        array[root_node_index], array[biggest_value_index] = array[biggest_value_index], array[root_node_index]     # Indeks rodzica posiada największą wartość, wartość rodzica przechodzi do dziecka

        # Rekurencja aby przejść przez całe drzewo
        heapify(array, array_length, biggest_value_index)


def heap_sort(array):
    length = len(array)

    for i in range(length//2, -1, -1): # Iteracja od dołu drzewa
        heapify(array, length, i)

    for i in range(length-1, 0, -1):   # Zamiana największego elementu z najmniejszym i wstawienie największego na koniec listy
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    print(array)


arr = [21, 12, 11, 13, 5, 20, 6, 7, 20]
heap_sort(arr)
