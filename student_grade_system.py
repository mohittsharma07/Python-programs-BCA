# print student marks :-

marks = int(input("Enter student marks: "))

if(marks >= 90):
    grade = "A"

elif(marks >= 70 and marks < 90):
    grade = "B"

elif(marks >= 50 and marks < 70):
    grade = "C"

else:
    grade = "D"

print("grade of the student :", grade)
