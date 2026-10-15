def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr, left, right):
    # Рекурсивно обрабатываем меньшую часть, чтобы не переполнить стек.
    while left < right:
        pivot_index = partition(arr, left, right)
        if pivot_index - left < right - pivot_index:
            _quick_sort(arr, left, pivot_index - 1)
            left = pivot_index + 1
        else:
            _quick_sort(arr, pivot_index + 1, right)
            right = pivot_index - 1
