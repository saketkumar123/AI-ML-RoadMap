# Part 1: Conditional Statements

# Exercise 1: Simple if
age = 18

if age >= 18:
    print("Eligible to vote") 

# Exercise 2: if-else
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    

# Exercise 3: if-elif-else
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
    
# Exercise 4: Multiple Conditions
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successfully")
else:
    print("Invalid Credentials")
    

# Part: 2 Loops
# Exercise 1: for Loop
for i in range(5):
    print(i)
    
# Exercise 2: print 1 to 10
for i in range(1, 11):
    print(i)
    
# Exercise 3: Multiplication Table
number = 5

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
    
# Exercise 4: Loop Through a list
print("Loop Through a list")
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
    
# Exercise 5: while Loop
print("While loop")
count = 1
while count <= 5:
    print(count)
    count += 1
    
# Exercise 6: break
print("break")
for i in range(1, 11):
    if i == 6:
        break
    print(i)
    
# Exercise 6: continue
print("continue")
for i in range(1, 11):
    if i == 6:
        continue
    print(i)