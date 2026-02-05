listdata = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search = int(input("Please type number, looking for: "))
found = False
for i in listdata:
    if i == search:
        found = True
        break


if found:
    print(f"number {search} is in the List!")
else:
    print(f"number {search} is not found!")
    
