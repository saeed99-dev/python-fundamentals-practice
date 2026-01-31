places=["Goa","Bihar","Mehsi","Itly","Peru","Delhi","Motihari","Gujrat","Manipur"]
name="Shivamsrivastav"

i=0
while i<len(name):
    name[::-1]
    i+=1
print(name[::-1])



city="Muzaffarpur"
reversed_city = ""
for char in city:
    reversed_city = char + reversed_city 
print(reversed_city)


state="Chattisgarh"
reversed_state = ""
for i in range(len(state) - 1, -1, -1):
    reversed_state += state[i]
print(reversed_state)
