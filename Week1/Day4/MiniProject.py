#marks = [85,90,78,92,88]
marks = []

for i in range(5):
    mark = int(input(f"Enter marks {i+1}: "))
    marks.append(mark)

average = sum(marks)/len(marks)

print("\nResult Summary")
print("----------------")
print(f"Marks: {marks}")
print(f"Highest Marks: {max(marks)}")
print(f"Lowest Marks: {min(marks)}")
print(f"Average: {round(average, 2)}")

if average >= 90:
    print("Grade A")
elif average >= 75:
    print("Grade B")
elif average >= 60:
    print("Grade C")
else:
    print("Fail")
    
if average >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")