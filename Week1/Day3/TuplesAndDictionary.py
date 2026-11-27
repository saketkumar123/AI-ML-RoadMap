# Part 1: Tuple
#Exercise 1: Create a Tuple
fruits = ("Apple", "Mango", "Banana")

print(fruits)

# Exercise 2: Access Tuple Elements
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Exercise 3: Tuple Length
print(len(fruits))

# Exercise 4: Loop through a Tuple
for fruit in fruits:
    print(fruit)
    
# Exercise 5: Tuple Immutability
# fruits[0] = "Litchi"

# Mini Practice
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(f"First Days: {days[0]}")
print(f"Last Days: {days[len(days)-1]}")
print(f"total days: {len(days)}")

# Part 2: Dictionary
# Exercise 1: Create Dictionary
student = {
    "name": "Saket",
    "age": 33,
    "city": "Bangalore"
}

print(student)

# Exercise 2: Access Values
print(student["name"])
print(student["age"])

# Exercise 3: Add New Data
student["dept"] = "CSE"
print(student)

# Exercise 4: Update Data
student["age"] = 35
print(student)

# Exercise 5: Loop through a Dictionary
for key, value in student.items():
    print(key, ":", value)