# append method
l1= ["Banana","cake","73.4","23","Zakariya","False","none"]
l1.append("Zakariya data scientist")
print(l1)

# sort method
l1=[ 83 , 43, 33 , 23 , 13 , 3]
l1.sort()
print(l1)

# reverse method
l1= [3,13,23,33,43,83]
l1.reverse()
print(l1)

# insert method
l1= [3,23,33,43,83]
l1.insert(2,53) 
print(l1)

# remove method 
l1= [3 , 23 , 33 ,37 ,43 , 83]
l1.remove(37)
print(l1)

# pop method 
l1= [3,34,33,43,55]
# l1.pop(3)         # this line cannot show me the return value
print(l1.pop(3))    # this line show me the return value   
print(l1)


# extend method 
l1=[1,2,3,4]
l2=[22,33,4,53,3]
l1.extend(l2)
print(l1)