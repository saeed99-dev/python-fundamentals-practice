import json
from datetime import datetime


def withdrow_cash():
    amount=200
    try:
        user_input=input("Please Enter amount to withdrow: ")
        
        if amount>=int(user_input):
            print(f"dispacthing Rs-{user_input}")
        else:
            print("Input amount is not available i your a/c")
    except Exception as e:
        print("Please Enter a valid amount type") 

        customerdata={
            "error":str(e),
            "datetime":str(datetime.now()),
            "function_name":"withdrow_cash",
            "withdrow_amount":user_input
        }
        
        with open("customerlog.txt","w") as file:
            json.dump(customerdata,file,indent=4)
            

withdrow_cash()

