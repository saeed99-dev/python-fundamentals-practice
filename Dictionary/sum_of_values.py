data = {'a': 1.5, 'b': 2.5, 'c': 3.0}

total_sum=0
for value in data.values():
    total_sum+=value

print(total_sum)



Player_data = {
    'points': 100,
    'bonus': 50,
    'name': 'Player1',
    'level': 5,
    'active': True
}
sum_total=0
for val in Player_data.values():
    if isinstance(val,(int,float)) and not isinstance(val,bool): #NOTE:( Booleans are technically ints, but we can filter them)
        sum_total+=val

print(sum_total)


data = {
    'sales_q1': 500,
    'sales_q2': {
        'january': 150,
        'february': 200,
        'march': 150
    },
    'expenses': {
        'fixed': 100,
        'variable': {
            'ads': 50,
            'shipping': 25
        }
    }
}

total = 0

for v1 in data.values():
    if isinstance(v1, (int, float)):
        total += v1
    elif isinstance(v1, dict):
        for v2 in v1.values():
            if isinstance(v2, (int, float)):
                total += v2
            elif isinstance(v2, dict):
                for v3 in v2.values():
                    if isinstance(v3, (int, float)):
                        total += v3

print(f"Grand Total: {total}")