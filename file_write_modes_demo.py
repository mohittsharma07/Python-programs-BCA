f = open("demo.txt", "w")

f.write("I want to learn python.1234...")
f.close()

print("\n-----------------")


f = open("demo.txt", "a")

f.write("\nhello guyssss...")
f.close()

print("\n-------------------")


f = open("demo.txt", "a")

f.write("abc")
f.close()


print("\n-------------------")

f = open("demo.txt", "r+")

f.write("abc")
print(f.read())
f.close()

print("\n------------------")


f = open("demo.txt", "w+")

print(f.read())
f.close()

print("\n------------------")


f = open("demo.txt", "w+")

print(f.read())
f.write("abc")
f.close()

print("\n------------------")


f = open("demo.txt", "a+")

print(f.read())
f.write("abc")
f.close()