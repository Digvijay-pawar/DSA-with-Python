# String Methods
# Split() & Join
s = "Geeks for geeks"
ls = s.split(" ")
print(s,"=>", ls)
s = ",".join(ls)
print(ls, "=>", s)

# startwith & endwith
s = "Geeks for geeks"
print(s.startswith("Geek"))
print(s.endswith("eeks"))
print(s.startswith("G", 3, 8))

# strip methods
s = "--geeksforgeeks--"
a = s.strip('-') # remove strip from both corners
print(a)
b = s.lstrip('-') # remove strip from left corner
print(b)
c = s.rstrip('-') # remove strip from right corner
print(c)
s = "   geeks   "
print(len(s))
s = s.strip()
print(len(s))

# find method
s = "geeksforgeeks"
s1 = "geeks"
print(s.find(s1))
print(s.find("gfg"))
