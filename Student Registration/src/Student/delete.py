from src.Student.file_mode import load_data,savedata
from src.Student.validation import valid_digit

def Delete_data():
    listdata=load_data()
    search_id=valid_digit("Please Enter Student's ID : ")
    for student in listdata:
        if search_id==student["id"]:
            listdata.remove(student)
            savedata(listdata)
            return 
        
        else:
            print("Student ID not Found!")



    # Delete_data()