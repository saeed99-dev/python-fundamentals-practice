info = {
    "name": "Saeed",
    "age": "27",
    "topics": ("dict", "sets"),
    "is_adult": True,
    "company_name": "Indixpert",
    "subject": ["phy", "chem", "mathematics"],
    12.9:92.64
}

print(info)
info["name"]="Saeed Habib" #replace "Saeed" with "Saeed Habib"
print(info["name"])
info["city"]="Mehsi"   #add a key "city" and its value "Mehsi"
print(info)

student_data={
    "name":"Saba",
    "roll":25,
    "section":"9B",
    "subjects":{
        "phy":87,
        "chem":92,
        "math":78,
        "bio":80
    }
}

left_dict={
    "age":23,
    "gender":"Femal"
}

print(student_data)
print(student_data["subjects"])
print(student_data["subjects"]["phy"])

print(student_data.keys())
print(len(student_data))
print(list(student_data.keys()))
print(len(list(student_data.keys()))) 
print(student_data.values())
print(list(student_data.values()))
print(student_data.items())
print(list(student_data.items()))
pairs=list(student_data.items())
print(pairs[0])

print(student_data["name"])  # this code will not run from here if name key is not existing and show error and the code written after this code which does has any errors will not run
print(student_data.get("name")) #But in this case if the key is not existing it show "None" and the code after this line will also run smoothly.

student_data.update(left_dict)
print(student_data)