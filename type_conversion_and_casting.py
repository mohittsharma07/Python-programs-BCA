  # Type Conversion Examples 

a = int("7")         # string to int (manual conversion / casting)
b = 4.25             # float

print("a:", a, "| type:", type(a))
print("b:", b, "| type:", type(b))
print("Sum (a + b):", a + b)   # implicit conversion


# Type Casting Examples 

a = 6.13             # float
b = str(a)           # float to string (manual casting)

print("a:", a, "| type:", type(a))
print("b(casted from a):",b,"| type:",type(b))