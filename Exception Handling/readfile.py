try:
    with open("first.txt","r") as file:
        file.read()
except Exception as e:
    print(e)