words = ["Python", "is", "fun", "to", "learn"]
for w in words:
    print(w,end=" ")



words = ["Python", "is", "fun", "to", "learn"]
sentence = ""

for w in words:
    sentence += w + " "
print(sentence.strip())



words = ["Python", "is", "fun", "to", "learn"]
sentence = " ".join(words)

print(sentence)