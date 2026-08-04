class Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def display_details(self):
        print("----- Student Details -----")
        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_no}")
        print(f"Department : {self.department}")
