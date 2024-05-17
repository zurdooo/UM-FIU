print("Activity # 1:")

exam1 = int(input("Enter the first exam score: "))
exam2 = int(input("Enter the first exam score: "))
exam3 = int(input("Enter the first exam score: "))
exam4 = int(input("Enter the first exam score: "))

examScoreWeightedList = [exam1,exam2,exam3,exam4]

print("Original Input List",examScoreWeightedList)

print("The average exam score list is:", sum(examScoreWeightedList)/len(examScoreWeightedList))

print("here is the Exam weighted list and the sum in points:")

examScoreWeightedList[0] = examScoreWeightedList[0] * 0.1
examScoreWeightedList[1] = examScoreWeightedList[1] * 0.2
examScoreWeightedList[2] = examScoreWeightedList[2] * 0.3
examScoreWeightedList[3] = examScoreWeightedList[3] * 0.4

print(f"Weighted score list {examScoreWeightedList} \nThe total points is {sum(examScoreWeightedList)}")

print("Activity # 2:")

from collections import namedtuple

Student = namedtuple("Student", "Name Age Major GPA")

firstStudent = Student("Maria Fernandez", "18", "Psychology", "3.5")
secondStudent = Student("John Doe", "19", "Mathematics", "3.9")
thirdStudent = Student("Mia Hernandez", "20", "Computer Engineer", "3.8")

print(f"First student info:{firstStudent}")
print(f"Second student info:{secondStudent}")
print(f"Third student info:{thirdStudent}")

firstStudent = ("Alex","20","Computer science","4.0")

print(f"First student info:{firstStudent}")

print("Activity # 3:")

courseInfo = {"CSC-115": "TBA", "CSC-120": "TBA", "CSC-220":"TBA"}

courseInfo["CSC-115"] = "LC-170"
courseInfo["CSC-120"] = "LC-160"
courseInfo["CSC-220"] = "LC-150"

print(f"There are 3 courses in the courseInfo dictionary. \n{courseInfo}")
print(courseInfo.keys())
print(courseInfo.values())



