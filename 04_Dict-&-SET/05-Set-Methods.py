s= {2,3,3,4,5,"Khan",}

# method 1
s.add(200)
s,type(s)    
print(s)

# method 2
s.remove("Khan")
print(s,type(s))    


# method 3
# s.clear()
# print(s,type(s))      

# method 4
s.pop()
print(s,type(s))      

# method 5
print(len(s))    


# super set and subset , issubset ,issuperset  method 6

# print=(s.issubset(s)) 
a = {1, 2,3 ,4,}
b = {1, 2, 3, 4,5}

print(b.issuperset(a))   # True

