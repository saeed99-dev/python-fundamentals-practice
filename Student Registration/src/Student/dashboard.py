from src.Student.menu import registration_menu
from src.Student.registration import Registation
from src.Student.search import search_student
from src.Student.update import Update_records
from src.Student.delete import Delete_data
from src.Student.view import Display_info


def Dashboard():
    while True:
        option=registration_menu()
        if option==1:
            Registation()
        elif option==2:
            search_student()
        elif option==3:
            Update_records()
        elif option==4:
            Delete_data()
        elif option==5:
            Display_info()
        elif option==6:
            print("Taking Exit!")
            break
        else:
            print("Error! Please select option carefully")





