text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Vowel count: {count}")


text = "Python Programming"
vowel_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for char in text.lower():
    if char in vowel_counts:
        vowel_counts[char] += 1

print(vowel_counts)


text = "Artificial Intelligence"
# We create a list of characters only if they are vowels
count = len([char for char in text if char.lower() in "aeiou"])

print(f"Total vowels: {count}")


text = "Learning is fun"
text = text.lower()
total = sum(text.count(v) for v in "aeiou")

print(f"Total vowels: {total}")