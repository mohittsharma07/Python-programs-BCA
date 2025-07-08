# 1) Write a program to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one. use subject name as key and marks as value.

marks = {}

x = int(input("Enter math: "))
marks.update({"math": x})

x = int(input("Enter chem: "))
marks.update({"chem": x})

x = int(input("Enter phy: "))
marks.update({"phy": x})

print(marks)



# 2) Figure out a way to store 7 & 7.0 as separate values in the set. ( ypu can take help of built-in data type).

values = {
    ("float", 7.0),
    ("int",7)
}
print(values)


# 3) Figure out a way to store 7 & 7.0 as separate values in the set.

values = {7, "7.0"}
print(values)


# 4) store following word meaning in a python dictionary:- table: "a piece of furniture", list of facts & figures", cat:" a small animal".

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts & figures"]
}

print(dictionary)