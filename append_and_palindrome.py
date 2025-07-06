# Program 1: Write a program to ask the user to enter name of their 3 favorite games and store them in a list.

games = []
games.append(input("Enter 1st game: "))
games.append(input("Enter 2nd game: "))
games.append(input("Enter 3rd game: "))

print("your favorite games",games)


# Program 2: Write a program to check if a list contains a palindrome of elements. (use copy() method).

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not a palindrome")