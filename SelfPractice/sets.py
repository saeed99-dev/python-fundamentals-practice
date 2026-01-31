collection = {1,2,3,4,5,6,7,"Hello","S","S"}

print(collection)
print(type(collection))
print(len(collection))

empt=set()  #empty set is written this way (with paranthesis ,but not with curley braces )
            #set is mutable i.e we can add/remove elements but not replace elements i.e sets elements are immutable
print(type(empt))
empt.add(1)
empt.add(2)
empt.add(2)
empt.add("hello")
print(empt)
empt.remove(1)
print(empt)
empt.add((3,4,5,6))
print(empt)
print(empt.pop()) # eliminate/remove random value
print(collection.union(empt)) #combine both sets (collection & empt) values and return new
print(collection.intersection(empt)) #combines common values of both sets and returns new
empt.clear()  # it make a set empty i.e erase all elemets of a set
print(empt)
print(len(empt))


