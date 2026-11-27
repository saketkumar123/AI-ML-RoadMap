employee = {
    "id": 101,
    "name": "Saket",
    "salary": 50000
}

print(employee)

employee["department"] = "FS"
employee["salary"] += 5000
print(employee)

for key, value in employee.items():
    print(key," : ",value)