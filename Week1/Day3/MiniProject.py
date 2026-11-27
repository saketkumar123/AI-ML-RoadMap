student = {
    "name": "Saket",
    "age": 33,
    "city": "Bangalore",
    "course": "python"
}

print("Student Details")

for key, value in student.items():
    print(f"{key} :  {value}")

student["marks"] = 93
student["email"] = "abc@gmail.com"
student["mobile"] = 1234567898

print("After Enhance more details")

for key, value in student.items():
    print(f"{key} :  {value}")