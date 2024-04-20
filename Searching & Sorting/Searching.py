arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

key = int(input("Enter a number: "))

# 1) Linear Search => O(n)
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return "Found at " + str(i + 1) + "th Position"
    return "Not Found"

# result = linear_search(arr, key)
# print(result)


# 2) Binary Search Using Iterative Method => O(log n), O(1)

def binary_search_iterative(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return "Found at " + str(mid + 1) + "th Position"
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"

# result = binary_search_iterative(arr, key)
# print(result)

# 3) Binary Search Using Reccursive Method => O(log n), O(log n)
def binary_search_recursive(arr, key, low = 0, high = len(arr) - 1):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return "Found at " + str(mid + 1) + "th Position"
        elif arr[mid] < key:
            low = mid + 1
            binary_search_recursive(arr, key, low, high)
        else:
            high = mid - 1
            binary_search_recursive(arr, key, low, high)
    return "Not Found"

# result = binary_search_recursive(arr, key)
# print(result)

# Menu to select searching algorithm
ch = int(input("***********MENU*************\n1 for Linear search,\n2 for Recursive binary search,\n3 for Iterative binary search: \nChoose a Search: "))

if ch == 1:
    print("Array => " + str(arr))
    print("Key => " + str(key))
    print("Result =>" , linear_search(arr, key))
elif ch == 2:
    print("Array => " + str(arr))
    print("Key => " + str(key))
    print("Result =>", binary_search_recursive(arr, key))
elif ch == 3:
    print("Array => " + str(arr))
    print("Key => " + str(key))
    print("Result =>", binary_search_iterative(arr, key))
else:
    print("Invalid Choice")