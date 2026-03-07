import requests
import json

class API:
    def __init__(self):
        self.url_data="https://jsonplaceholder.typicode.com/comments"
    
    def get_data(self):
        try:
            data=requests.get(self.url_data)
            return data.json()
        except Exception as e:
            print(e)

    
    def search_data(self):
        input_email=input("Please enter Your email: ")

        datalist=self.get_data()

        found=False
        
        for item in datalist:
            if input_email==item["email"]:
                print(json.dumps(item,indent=4))
                found=True
                break
    
        if not found:
            print("Record not Found")

    def user_menu(self):
        print("1. Get Data")
        print("2. Search Data")
        print("3. Exit")

    def dashbord(self):
        while True:
            self.user_menu()
            try:
                option=int(input("Please Select your Option: "))

                if option==1:
                    print(json.dumps(self.get_data(),indent=4))
                elif option==2:
                    self.search_data()
                elif option==3:
                    print("Taking Exit..")
                    break
                else:
                    print("Please Enter valid Option")  
            except Exception as e:
                print(e)
req=API()
req.dashbord()