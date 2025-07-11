f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

print("\n-----------------------")


f = open("demo.txt", "r")

line1 = f.readline()
print(line1)
f.close()


print("\n-----------------------")


f = open("demo.txt", "r")

data = f.read(6)
print(data)
f.close()