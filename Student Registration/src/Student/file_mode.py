import json
import os

filename="student_data.json"
def create_file():
    if not os.path.exists(filename):
        with open(filename,"w") as file:
            json.dump([],file)


def load_data():
    create_file()
    with open(filename,"r") as file:
        listdata=json.load(file)
    return listdata





def savedata(listdata):
    with open(filename,"w") as file:
        json.dump(listdata,file, indent=4)
