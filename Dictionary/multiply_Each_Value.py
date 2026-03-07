#Multiply all numerical values in a dictionary by 10
data = {'a': 1.5, 'b': 2.5, 'c': 3.0}
key_update=[]
value_update=[]
for key,value in data.items():
    key_update.append(key)
    value_update.append(10*value)

print(dict(zip(key_update,value_update)))

                    #OR


for key in data:
    data[key]=data[key]*10

print(data)


data = {
    'level1_val': 5,
    'info': {
        'level2_val': 10,
        'other_val': 20
    }
}

for key,value in data.items():
    if isinstance(value,(int,float)):
        data[key]=data[key]*10
    elif isinstance(value,dict):
        for sub_key,sub_value in value.items():
            if isinstance(sub_value,(int,float)):
                value[sub_key]=value[sub_key]*10

print(data)