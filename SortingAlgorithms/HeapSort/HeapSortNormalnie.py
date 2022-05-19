with open('input.txt', 'r') as file:
    tablica = [int(line) for line in file]

def heapify(arr, arr_length, root_node_index):                                     # Tablica, długość tablicy, indeks rodzica

    biggest_value_index = root_node_index                                              # Definiuję największą wartość poddrzewa jako ideks rodzica (nie wiadomo czy jest największa, ale taka powinna być)
    left_child = root_node_index * 2 + 1                                               # Lewe dziecko w poddrzewie
    right_child = root_node_index * 2 + 2                                              # Prawe dziecko w poddrzewie

    if left_child < arr_length and arr[left_child] > arr[biggest_value_index]:   # Sprawdzam czy istnieje lewe dziecko, następnie sprawdzam czy lewe dziecko jest większe od rodzica
        biggest_value_index = left_child                                               # Nie arr[left_child], bo wtedy przypisuję wartość a nie indeks
                                                                                       # co powoduje problem przy rekurencji oraz swapowaniu w 3 if'

    if right_child < arr_length and arr[right_child] > arr[biggest_value_index]: # Sprawdzam czy istnieje prawe dziecko, następnei sprawdzam czy prawe dziecko jest większe od rodzica
        biggest_value_index = right_child

    if root_node_index != biggest_value_index:                                         # Jeśli rodzic nie ma największej wartości to zamieniam go z elementem o największej wartości
                                                                                       # (zamieniam wartości dla konkretnych indeksów a nie indeksy)

        arr[root_node_index], arr[biggest_value_index] = arr[biggest_value_index], arr[root_node_index]     # Indeks rodzica posiada największą wartość, wartość rodzica przechodzi do dziecka

        # Rekurencja aby przejść przez całe drzewo
        heapify(arr, arr_length, biggest_value_index)


def heap_sort(arr):
    length = len(arr)

    for i in range(length//2, -1, -1):                                                  # Iteracja od dołu drzewa
        heapify(arr, length, i)

    for i in range(length-1, 0, -1):                                                    # Zamiana największego elementu z najmniejszym i wstawienie największego na koniec listy
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    with open('output.txt', 'w') as file:
        for line in arr:
            file.write(str(line))
            file.write('\n')

    print(arr)

heap_sort(tablica)
