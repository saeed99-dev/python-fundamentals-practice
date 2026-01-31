name = input("Please Enter Your Name: ")
vowels = "aeiou"

total_vowel=[char for char in name.lower() if char in vowels]
print(f"Total vowel in Your name is {len(total_vowel)} which is {total_vowel}")
