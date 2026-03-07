#Q. Create a dictionary from a string where keys are characters and values are their index.
name="SAeedhabib"
key=[]
value=[]
i=0
for char in name:
    i+=1
    key.append(char)
    value.append(i)

print(dict(zip(key,value)))



#Q. Create a dictionary from a string where keys are characters and values are their frequencies.
text = "characteristics"
frequencies = {}

for char in text:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

print(frequencies)



fruit = "banana"  
frequencies = {}

for char in fruit:
    frequencies[char] = frequencies.get(char,0) + 1

print(frequencies)



from collections import Counter

text = "mississippi"
frequencies = Counter(text)

print(dict(frequencies))
