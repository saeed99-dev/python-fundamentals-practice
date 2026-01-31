num = 29
is_prime = True

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



num = 17

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
else:
    print(f"{num} is not prime")




# Why check only up to the square root (sqrt{n}
# ?If a number n has a divisor, at least one of those divisors must be less than or equal to sqrt{n}. 
    # For example, to check if 36 is prime:sqrt{36} = 6.If you don't find a divisor by 6, you won't find one higher (like 9 or 12) because they would have been paired with a smaller number (4*9 or 3*12).