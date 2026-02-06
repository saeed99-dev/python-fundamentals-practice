# Question= Given a string, move all uppercase characters to the front

greet="GoOdNigHT"
upper=""
lower=""

for x in greet:
    if x.isupper():
        upper+=x
    else:
        lower+=x

sort_greet=upper+lower
print(sort_greet)