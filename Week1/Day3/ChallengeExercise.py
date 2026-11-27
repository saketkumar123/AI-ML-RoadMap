students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78
}

highest_student = max(students, key=students.get)
lowest_student = min(students, key=students.get)

average = sum(students.values()) / len(students)

print("Highest", highest_student, students[highest_student])
print("Lowest", lowest_student, students[lowest_student])
print("Average", average)