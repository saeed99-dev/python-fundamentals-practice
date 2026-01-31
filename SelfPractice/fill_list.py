new_list=[]
for i in range(1,11):
    new_list.append(i)
print(new_list)


num=[]
i=1
while i<=10:
    num.append(i)
    i+=1

print(num)


numbers = []

for i in range(1, 11):
    # Concatenate the current list with a new single-item list
    numbers = numbers + [i]

print(numbers)



# Create a list of 10 zeros first
numbers = [0] * 10

# Use a loop to assign values to specific indices
for i in range(10):
    # index 0 gets 1, index 1 gets 2, etc.
    numbers[i] = i + 1

print(numbers)


# Pre-allocate a list of 10 zeros
squares = [0] * 10

# Loop from 0 to 9
for i in range(10):
    # Calculate the square (index + 1) squared
    number_to_square = i + 1
    squares[i] = number_to_square ** 2
    
print(squares)