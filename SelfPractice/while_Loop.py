square = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index < len(square):
    print(square[index])
    index += 1


count=1
while count<=5:
    print("Hello", count)
    count+=1
print(count)

i=1
while i<=100:
    print(i)
    i+=1

i=100
while i>0:
    print(i)
    i-=1

n = int(input("please enter any number: "))
count = 1
while count <= 10:
    print(f"{n} x {count} = {n*count}")
    count += 1

square = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index < len(square):
    print(square[index])
    index += 1


square = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Please enter element : "))
i = 0
while i < len(square):
    if (square[i] == x):
        print("found at Index", i)
    i += 1


i=1
while i<=10:
    print(i)
    if (i==5):
        break  
    i +=1

print("Loop Ended!")

i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue  
    print(i)
    i += 1

print("Loop Ended!") 
