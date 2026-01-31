data={"name":"Saeed","age":26,"address":"Mehsi"}
number=[2,3,5,7,9,22,55,88,11,45,98,1,4]
max=number[0]
for i in range(1,len(number)):
    if max<number[i]:
        max=number[i]

print(max)


number=[2,3,5,7,9,22,55,88,11,45,98,1,4]
max=number[0]
for element in number:
    if max<element:
        max=element

print(max)


numbers = [-50, -12, -88, -5]
largest = None

for n in numbers:
    if largest is None or n > largest:
        largest = n

print(f"The largest negative number is: {largest}")