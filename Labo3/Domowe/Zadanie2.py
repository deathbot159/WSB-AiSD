a = [1, 5, 6, 2, 5, 4, 3, 6, 8, 9]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


print(f"Ins: {insertion_sort(a)}")
