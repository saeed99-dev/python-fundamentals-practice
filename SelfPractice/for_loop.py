nums=[1,2,3,4,5,6,7,8]

for x in nums:
    print(x)

veggies=["potato", "brinjal","ladyfinger","cucumber"]

for el in veggies:
    print(el)

str="Saeed Habib"

for char in str:
    print(char)
else:
    print("End")


sqr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 64
idx = 0
for ele in sqr:
    # print(ele)
    if ele == x:
        print(ele,idx)
    idx += 1


for i in range(100,0,-1):
    print(i)


n=10
sum=0
for i in range(1,n-1):
    sum+=i

print("total sum =",sum)


n = 10
sum = 0
j = 1
while j <= n:
    sum += j
    j+=1
print("total sum =", sum)


n = 5
fact = 1
i = 1
while i<=n:
    fact *= i
    i += 1

print("factorial =", fact)


n=10
fact=1
for i in range(1,n-1):
    fact*=i

print("factorial=",fact)