# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # Loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # TO-DO: Find next smallest element
        for j in range(current_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: Swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO: Implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# STRETCH: Implement the Count Sort function below
def count_sort(arr, maximum = -1):
    return arr