import numpy as np


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    test_array = np.array([10, 40, 20, 3, 4, 5, 6, 9, 92, 5, 3, 2, 5, 66])
    print(bubble_sort(test_array))
