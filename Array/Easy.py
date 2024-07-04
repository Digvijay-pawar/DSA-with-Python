# Smallest element in list
def smallest_item(l):
    small_no = l[0]
    for i in l:
        if i < small_no:
            small_no = i
    return small_no

print(smallest_item([0, 1, 1, 2, 3,-1, 4, 5]))

# Second smallest element in list
def second_smallest(l):
    first = second = l[0]
    for i in range(1, len(l)):
        if l[i] < first:
            second = first
            first = l[i]
    return second

print(second_smallest([0, 1, 1, 2, 3,-1, 4, 5]))

# Largest element in list
def largest_item(l):
    large = l[0]
    for i in l:
        if i > large:
            large = i
    return large

print(largest_item([0, 1, 1, 2, 3,-1, 4, 5]))

# Second largest element in list
def second_largest(l):
    first = second = l[0]
    for i in range(1, len(l)):
        if l[i] > first:
            second = first
            first = l[i]
    return second

print(second_largest([0, 1, 1, 2, 3,-1, 4, 5]))


