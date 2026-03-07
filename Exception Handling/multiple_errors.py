def multiply_by_ten(data):
    try:
        # ValueError: if data is a string like "hello"
        # TypeError: if data is a NoneType or a list
        result = float(data) * 10
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please provide a numeric string (e.g., '5').")
    except TypeError:
        print("Error: Input must be a string or a number, not a complex object.")

multiply_by_ten("abc")  # ValueError
multiply_by_ten([1, 2]) # TypeError



def check_voting_age(age):
    try:
        # ValueError: if age is "twenty"
        # TypeError: if age is a list [18]
        if int(age) >= 18:
            print("You can vote!")
        else:
            print("Too young.")
    except ValueError:
        print("Error: Could not understand the digits in your age.")
    except TypeError:
        print("Error: Age must be a single value, not a collection.")

check_voting_age("25")    # Success
check_voting_age("old")   # ValueError
check_voting_age(None)    # TypeError




def format_temperature(temp):
    try:
        # ValueError: if temp is "Cold"
        # TypeError: if temp is a dictionary
        celsius = float(temp)
        print("The temperature is {:.2f}°C".format(celsius))
    except ValueError:
        print("Error: Temperature must be a number.")
    except TypeError:
        print("Error: Unexpected data format provided.")

format_temperature({"temp": 32}) # TypeError
format_temperature("75.5")       # Success


