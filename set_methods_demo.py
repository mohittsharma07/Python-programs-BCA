# Set.add(el)...
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("Mohit sharma")
collection.add((1,2,3,4))

print(collection)
print(len(collection))



# Set.remove(el)...
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection.remove(1))
print(collection)



# Set.clear()...
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("Mohit sharma")

print(collection.clear())
print(len(collection))


# Set.pop()...
collection = {"Hello", "Mohit","sharma","coding","python"}

print(collection.pop())
print(collection.pop())


# Set.union(Set2)...
set1 = {1,2,4,6,7,9}
set2 = {2,3,5,8,9}

print(set1.union(set2))
print(set1)
print(set2)



# Set.intersection(Set2)...
set1 = {1,2,4,6,7,9}
set2 = {2,3,5,8,9}

print(set1.intersection(set2))
print(set1)
print(set2)
