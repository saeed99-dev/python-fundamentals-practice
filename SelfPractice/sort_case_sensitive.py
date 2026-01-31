fruits = ["Banana", "cherry", "litch", "Mango"]
print(
    sorted(fruits)
)  # this will sort firt Uppercase and then lowercase i.e. case sensitive
# By default, Python sorts using "lexicographical order" based on character codes. In the ASCII/Unicode table, all uppercase letters (A-Z) come before lowercase letters (a-z).

list = ["Banana", "cherry", "litch", "Mango"]
list.sort(key=str.lower)
print(list)

names = ["Zoe", "alice", "Charlie", "bob"]
names.sort(key=str.lower)
print(names)


