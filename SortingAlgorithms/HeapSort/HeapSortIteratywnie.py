with open('input.txt', 'r') as file:
    tablica = [int(line) for line in file]


def heapify_iterative(arr, n):

    for i in range(n):

        if arr[i] > arr[int((i-1)/2)]:
            j = i

            while arr[j] > arr[int((j-1)/2)]:
                arr[j], arr[int((j-1)/2)] = arr[int((j-1)/2)], arr[j]

                j = int((j-1) / 2)

def heapsort_iterative(arr, n):

    for i in range(n, 0, -1):
        heapify_iterative(arr, i)
        arr[0], arr[i-1] = arr[i-1], arr[0]

    with open('output.txt', 'w') as file:
        for line in arr:
            file.write(str(line))
            file.write('\n')

    print(arr)

heapsort_iterative(tablica, len(tablica))
