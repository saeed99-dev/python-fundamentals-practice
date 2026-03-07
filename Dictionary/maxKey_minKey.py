#Q. Find the maximum value in a dictionary.
data={'a':10,'b':13,'c':9,'d':3,'e':34}
max_value=0
for v in data.values():
    if max_value<v:
        max_value=v

print(max)


#Q. Find the minimum value in a dictionary

data={'a':10,'b':13,'c':9,'d':3,'e':34}
min_val=999
for val in data.values():
    if min_val>val:
        min_val=val

print(min)



#Q. Find the 'key' with the maximum value in a dictionary
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
max_key = None
max_value = float('-inf')

for key, value in scores.items():
    if value > max_value:
        max_value = value
        max_key = key

print(f"{max_key} has Max Key whoes value is {max_value}")


#Q. Find the 'key' with the minimum value in a dictionary
players_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}
min_key=None
min_value=float("inf")

for key,value in players_scores.items():
    if min_value>value:
        min_value=value
        min_key=key

print(f"{min_key} has Max Key whoes value is {min_value}")


player_scores = {'Alice': 95, 'Bob': 92, 'Charlie': 78, 'Diana': 95}

high_score=max(player_scores.values())

for key in player_scores.keys():
    if player_scores[key]==high_score:
        print(key)