a = [4, 5, 7, 7, 8, 6, 1, 4]


def bubble_sort(arr):
    for k in range(len(arr)):
        changed = False
        for i in range(len(arr) - k):
            if len(arr) - k - 1 != i and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
        if not changed:
            break

    return arr


print(sorted(a))
print(bubble_sort(a))
