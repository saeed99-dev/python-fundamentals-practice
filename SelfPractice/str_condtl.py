str1 = "Saeed"
str2 = "Habib"
final_str = str1 +" "+ str2



print(final_str)  #outcome= Saeed Habib 
print(len(final_str)) #outcome= 11

print(final_str[4]) #outcome= d
print(final_str[0:5]) #outcome= Saeed    "OR"
print(final_str[:5]) #outcome=  Saeed
print(final_str[2:5]) #outcome= eed
print(final_str[6:12]) # outcome= Habib  "OR"
print(final_str[6:len(final_str)])  # outcome= Habib   "OR"
print(final_str[6:]) # outcome= Habib
print(final_str[-9:-2]) # outcome= eed Hab


name=input("Enter Your name:")
print(len(name))
