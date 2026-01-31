number="2637976"
sum=0
for i in number:
    sum=sum+int(i)

print("sum_of_digits=",sum)



n = abs(int(input("Please Enter any number(>2 digits): ")))
total_sum = 0
while n > 0:
    total_sum += n % 10
    n //= 10

print("sum_of_digits=",total_sum)