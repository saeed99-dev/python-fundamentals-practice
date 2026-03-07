from datetime import datetime
import json

def Division():
    try:
        num1=int(input("please Enter 1st number: "))
        num2=int(input("please Enter 2nd number: "))

        result=num1/num2
        print(f"sucess:{num1}/{num2}={result}")
    except Exception as e:
        datalog={
            "error":str(e),
            "time":str(datetime.now()), 
            "function_name":"Division",
            "1st number":num1,
            "2nd number":num2
        }
        
        with open("datalog.txt","w") as file:
            json.dump(datalog,file)


Division()