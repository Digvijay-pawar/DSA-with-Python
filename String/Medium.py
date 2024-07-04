def pattern_matching(txt, pattern):
    i = j = 0
    while i < len(txt) and j < len(pattern):
        if j == len(pattern):
            return True
        if txt[i] == pattern[j]:
            j += 1
        else:
            j = 0
        i += 1
    return False


print(pattern_matching("geeksforgeeks", "org"))