from student import Student
from marks import calculate_grade
from attendance import attendance_percentage

# Student Details
student = Student("Rahul", 101, "Computer Science")

# Marks
marks = [85, 90, 78, 88, 92]
average, grade = calculate_grade(marks)

# Attendance
attendance = attendance_percentage(90, 100)

# Display Report
student.display_details()

print("\n----- Academic Report -----")
print("Marks:", marks)
print(f"Average Marks : {average:.2f}")
print(f"Grade         : {grade}")

print("\n----- Attendance -----")
print(f"Attendance Percentage : {attendance:.2f}%")
