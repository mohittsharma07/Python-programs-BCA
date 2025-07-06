# myDict.keys()...
info = {
    "name" : "Mohit sharma",
    "age"  : 19,
    "is adult" : True,
    "marks"  : 94.4,
    "learning" : "coding",
}

print(info.keys())
print(len(list(info.keys())))


# myDict.values()...
info = {
    "name" : "Mohit sharma",
    "age"  : 19,
    "is adult" : True,
    "marks"  : 94.4,
    "learning" : "coding",
}

print(info.values())



# myDict.items()...
student = {
    "name" : "Mohit sharma",
    "subjects" : {
        "phy" : 87,
        "chem" : 98,
        "maths" : 90
    }
}

print(student.items())
print(list(student.items()))
pairs = list(info.items())
print(pairs[0])


# myDict.get("key")...
student = {
    "name" : "Mohit sharma",
    "subjects" : {
        "phy" : 87,
        "chem" : 98,
        "maths" : 90
    }
}

print(student.get("name"))



# myDict.update(newDict)...
student = {
    "name" : "Mohit sharma",
    "subjects" : {
        "phy" : 87,
        "chem" : 98,
        "maths" : 90
    }
}

student.update({"city" : "kanpur"})

new_dict = {"age":19}
student.update(new_dict)

print(student)