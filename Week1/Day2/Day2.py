# Day: 2
# String
#Exercise: 1 Creating String

print(name)
print(city)

#Exercise: 2 String Concatenation
first_name = "Saket"
last_name = "Kumar"
full_name = first_name + " " + last_name;
print(full_name)

#Exercise: 3 f-String(Important)
name = "Keerat"
role = "Software Engineer"

print(f"My name is {name}")
print(f"I am a {role}")

#Exercise: 4 Common String Methods
text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())

#Exercise: 5 String Length
name = "Kreeti Kumari"
print(len(name))

# Mini Challenge
name = input("Enter your full name: ")

print(f"Hello {name}")
print(f"your name has {len(name)} characters")

# Lists
# Exercise 1: Create a List

fruits = ["Apple", "Banana", "orange"]
print(fruits)

# Exercise 2: Access Elements
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Exercise 3: Add Elements
fruits.append("Mango")

print(fruits)

# Exercise 4: Remove Elements
fruits.remove("Banana")

print(fruits)

# Exercise 5: List Length
print(len(fruits))

# Exercise 6: Loop Through a list
for fruit in fruits:
    print(fruit)