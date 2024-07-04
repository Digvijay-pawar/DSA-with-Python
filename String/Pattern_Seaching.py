# #Simple Pattern Searching
# def pattern_serch(txt, pattern):
#     pos = txt.find(pattern)
#     while pos >= 0:
#         print(pos)
#         pos = txt.find(pattern, pos+1)
    
# pattern_serch("geeksforgeeks", "geeks")

# #Neive pattern searching
# def neive_pattern(txt, pattern):
#     n, m = len(txt), len(pattern)
#     for i in range(n - m + 1):
#         j = 0
#         while j < m:
#             if pattern[j] != txt[i + j]:
#                 break
#             j += 1
#         if j == m:
#             print(i)
            
# neive_pattern("abababcd", "abab")

#Neive pattern searching for distinct pattern
def neive_pattern1(txt, pattern):
    n, m = len(txt), len(pattern)
    i = 0
    while i <= (n - m):
        j = 0
        while j < m:
            if txt[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            print(i)
        if j == 0:
            i += 1
        else:
            i += j
        
neive_pattern1("abcabcd", "abcd")
