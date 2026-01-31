word="Python"
for i in range(len(word)):
    print(f"{i}={word[i]}")



word = "Python"
index = 0
for char in word:
    print(f"Index {index}: {char}")
    index += 1



word = "Python"
i = 0

while i < len(word):
    print(f"{word[i]}:{i}")
    i += 1
    

word = "Python"
for index, char in enumerate(word):
    print(f"Index {index}: {char}")