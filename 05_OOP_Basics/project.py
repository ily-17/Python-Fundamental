class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


student1 = Student("Shirley", 25)
student2 = Student("John", 22)

student1.display()
print("-" * 20)
student2.display()

###Name: Shirley
Age: 25
--------------------
Name: John
Age: 22###
