arr = [10, 20, 30, 40]

# def reverse(arr):
#     i, j  = 0, len(arr)-1
#     while i < j:
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1
#         j -= 1
#     return arr


# def reverse_upto_index(arr, k):
#     new_arr = arr[:k+1]
#     return reverse(new_arr) + arr[k+1:]

# print(reverse_upto_index(arr, 2))


# def rotate(arr, k):
#     diff = len(arr) - k
#     return arr[diff:] + arr[:diff]

# print(rotate(arr, 2))
 
# def binary_search(arr, low, high, item):
    
#     if low <= high:
#         mid = low + (high - low) // 2
#         if arr[mid] == item:
#             return mid
#         elif arr[mid] < item:
#             return binary_search(arr, low, mid-1, item)
#         else:
#             return binary_search(arr, mid + 1, high, item)
#     else:
#         return -1
    
# print(binary_search([1, 2, 3, 3, 6],0, 4, 6))

def func(arr, x):
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            high = mid - 1
        else:
            low = mid + 1

print(func([1, 2, 3, 5, 6], 1))    
        
    