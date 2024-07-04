# reverse string without method
s = "geeks"
rev = ""
for i in s:
    rev = i + rev
print(rev)    

a = "abcd"
b = "cdab"

if len(a) != len(b):
    print("Not rotation")
temp = a + b
print(temp.find(b))


# Check palindrome
def check_palindrome(s):
    low, high = 0, len(s)-1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            return "Not palindrome"
    return "Palindrome"

print(check_palindrome("Adda"))
print(check_palindrome("adda"))
print(check_palindrome("ada"))

# Check if a String is Subsequence of Other
def check_substring(s, sub):
    i = j = 0
    while i < len(s) and j < len(sub):
        if s[i] == sub[j]:
            i += 1
            j += 1
        else:
            i += 1

    if j == len(sub):
        return "Substring"
    else:
        return "Not-Substring"
print(check_substring("abcde", "de"))

def check_anagram(s1, s2):
    for i in s1:
        if i in s2:
            continue
        else:
            return False
    return True

print(check_anagram("listen", "silent"))