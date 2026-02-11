#create a class called student with the following attributes fullname, course ,age ,fees, paid

#create multiple objects create at least three student  objects from the same class with different values and display the same information



class Student:
    def __init__(self, fullname, course, age, fees, paid):
        self.fullname = fullname
        self.course = course
        self.age = age
        self.fees = fees
        self.paid = paid


    def display_info(self):
        print("Full Name:", self.fullname)
        print("Course:", self.course)
        print("Age:", self.age)
        print("Fees:", self.fees)
        print("Paid:", self.paid)
        print("-" * 30)

print()
student1 = Student("Alice Johnson", "Computer Science", 20, 50000, 30000)
student2 = Student("Brian Smith", "Business Administration", 22, 45000, 45000)
student3 = Student("Catherine Lee", "Engineering", 21, 60000, 40000)

print()
student1.display_info()
student2.display_info()
student3.display_info()