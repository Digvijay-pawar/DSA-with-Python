# Check if list is sorted or not
def is_sorted(l):
    if len(l) <= 1: 
        # if array has 1 or no element
        return True
    for i in range(len(l) - 2):
        if l[i+1] > l[i]:
            continue
        else:
            return False
    return True

print(is_sorted([1, 0, 3, 4, 5]))

# Reverse a list
def reverse_list(ls):
    last = len(ls) - 1
    first = 0
    while first != last:
        temp = ls[first]
        ls[first] = ls[last]
        ls[last] = temp
        first += 1
        last -= 1
    return ls

print(reverse_list([1, 2, 3, 4, 5]))