from collections import namedtuple

alex = ("Alex Ramos", "Alex@miami.edu","Computer Sci")

Student = namedtuple("Student",["name","email","major"])

alex_student = Student("Alex Ramos","axr@miami.edu","Computer Science")

print(alex_student[0])
print(alex_student.name)
print(alex_student.email)
print(alex_student.major)