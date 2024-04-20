arr = [23, 1, 10, 5, 2]

# Insertion Sort => O(n^2), O(1)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key <  arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(arr))

"""
Time Complexity of Insertion Sort
    Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
    Average case: O(n2), If the list is randomly ordered
    Worst case: O(n2), If the list is in reverse order

Space Complexity of Insertion Sort
    Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.

Advantages of Insertion Sort:
    - Simple and easy to implement.
    - Stable sorting algorithm.
    - Efficient for small lists and nearly sorted lists.
    - Space-efficient.

Disadvantages of Insertion Sort:
    - Inefficient for large lists.
    - Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.

Applications of Insertion Sort:
    - Insertion sort is commonly used in situations where:
    - The list is small or nearly sorted.
    - Simplicity and stability are important.

"""

# Selection Sort => O(n^2)
def selection_sort(arr):  
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


"""
Complexity Analysis of Selection Sort
    Time Complexity: 
        The time complexity of Selection Sort is O(N2) as there are two nested loops:

        - One loop to select an element of Array one by one = O(N)
        - Another loop to compare that element with every other Array element = O(N)
        - Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)
    Auxiliary Space: 
        O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The selection sort never makes more than O(N) swaps and can be useful when memory writing is costly. 

Advantages of Selection Sort Algorithm
    - Simple and easy to understand.
    - Works well with small datasets.

Disadvantages of the Selection Sort Algorithm
    - Selection sort has a time complexity of O(n^2) in the worst and average case.
    - Does not work well on large datasets.
    - Does not preserve the relative order of items with equal keys which means it is not stable.

"""


# Quick Sort => 
def partition(arr, low, high):
    pivot = arr[high]
    j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i] 
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j   

# print(partition([10, 80, 30, 90, 40]))  

def quick_sort(arr, low=0, high=len(arr)-1):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    else:
        return arr

print(quick_sort([10, 80, 30, 90, 40]))
