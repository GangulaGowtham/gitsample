# Create a set using curly braces
fruits = {"apple", "banana", "cherry"}

# Create an empty set (Note: {} creates an empty dictionary)
empty_set = set()

# 1. Add a single element
fruits.add("orange")  # {"apple", "banana", "cherry", "orange"}

# 2. Add multiple elements from another collection
fruits.update(["mango", "grapes"])

# 3. Duplicate values are automatically ignored
fruits.add("apple")  # Set remains unchanged

# 4. Remove an element (Raises KeyError if not found)
fruits.remove("banana")

# 5. Remove an element safely (Does nothing if not found)
fruits.discard("blueberry")

print("Final fruits set:", fruits)
