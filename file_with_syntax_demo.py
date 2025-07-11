with open("demo.txt" , "r") as f:
    data = f.read()
    print(data)

print("\n------------------------")


with open("demo.txt" , "w") as f:
    f.write("new data")