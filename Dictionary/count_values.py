data = {"Alice": 25, "Bob": 30, "Charlie": 25, "David": 22}
target = 25
count = list(data.values()).count(target)
print(f"The value {target} appears {count} times.") 


from collections import Counter

data = {"item1": "apple", "item2": "banana", "item3": "apple", "item4": "orange"}

value_counts = Counter(data.values())  # count all values appearance
print(value_counts)
print(value_counts["apple"])  # count only apple appearance

