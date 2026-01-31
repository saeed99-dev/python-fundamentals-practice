marks=[12.5,26.25,34.2,19.7,6.75]
print(marks)
print(type(marks))
print(marks[2])
print(marks[0])

info=["Rahul",25,95,"Bihar"]
print(info)
print(type(info))
print(info[0])
info[0]="Asif"
print(info)
print(info[1:3])   #index slicing is possible in both +ve and _ve ways
info.append(845426)
print(info)
info.insert(1,"6th")
print(info)
info.pop(2)
print(info)

tup=(2,3,5,9,1,2,3,2)
print(type(tup))
print(tup[0])
print(tup.count(2))
print(tup.index(5))