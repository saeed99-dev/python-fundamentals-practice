name="shivam shrivastav"
vowel="aeiouAEIOU"
newstr=""
for char in name:
    if char in vowel:
        newstr+="*"
    else:
        newstr+=char
print(newstr)


sentance="Python Programming"
Vowel="aeiouAEIOU"
newStr=""
i=0
while i<len(sentance):
    if sentance[i] in Vowel:
        newStr+="*"
    else:
        newStr+=sentance[i]
    i+=1
print(newStr)
