# Using print() with multiple arguments
print("Name:", "Alice", "Age:", 25, "Country:", "India")

# Using f-string (Python 3.6+)
name = "Bob"
age = 30
country = "USA"
print(f"Name: {name} Age: {age} Country: {country}")

# Using .format() method
lang = "Python"
version = 3
print("You are learning {} version {}.".format(lang, version))

# Custom separator
print("Apple", "Banana", "Cherry", sep=", ")

# Printing variables directly
a, b, c = 10, 20, 30
print(a, b, c)
