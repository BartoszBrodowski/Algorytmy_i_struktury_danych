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

    print(arr)

arr = [21, 12, 11, 13, 5, 20, 6, 7, 20]
heapsort_iterative(arr, len(arr))
