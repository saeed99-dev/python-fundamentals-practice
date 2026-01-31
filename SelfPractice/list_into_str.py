fruits = ["apple", "banana", "litchi", "mango", "guava"]
string = "".join(fruits) # join without space (putcome: applebananalitchimangoguava)
print(string)

fruits = ["apple", "banana", "litchi", "mango", "guava"]
string = " ".join(fruits) # join with space (Outcome: apple banana litchi mango guava)
print(string)

fruits = ["apple", "banana", "litchi", "mango", "guava"]
string = ", ".join(fruits) # join with comma and space (Outcome: apple, banana, litchi, mango, guava)
print(string)
