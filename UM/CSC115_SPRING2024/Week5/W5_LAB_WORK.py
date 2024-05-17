print("Activity # 1:")

exam1 = float(int(input("Enter the first exam score: ")))
exam2 = float(int(input("Enter the second exam score: ")))
exam3 = float(int(input("Enter the third exam score: ")))
exam4 = float(int(input("Enter the fourth exam score: ")))

examScore = [exam1, exam2, exam3, exam4]
examScoreWeightedList = [exam1 * 0.1, exam2 * 0.2, exam3 * 0.3, exam4 * 0.4]


print("Original Input List", examScore)

print()

print("Here is the Exam weighted list and the sum in points:")
totalPoints = sum(examScoreWeightedList)
print(
    f"Weighted score list {examScoreWeightedList} \nThe total points is {totalPoints}"
)

if totalPoints >= 90:
    print("Your final  grade is A.")
elif totalPoints >= 80:
    print("Your final grade is B.")
elif totalPoints >= 70:
    print("Your final  grade is C.")
elif totalPoints >= 60:
    print("Your final  grade is D.")
else:
    print("Your final  grade is F.")

print("Activity # 2:")

from datetime import date

yearBorn = int(input("Enter the year you were born: "))

age = date.today().year - yearBorn

if age <= 1:
    print("Infant")
elif age <= 13 and age >= 1:
    print("Child")
elif age >= 13 and age <= 20:
    print("Teenager")
elif age >= 20 and age <= 65:
    print("Adult")
else:
    print("Senior")

print("Activity # 3:")

firstWidth = int(input("Enter the first width: "))
firstLength = int(input("Enter the first length: "))

secondWidth = int(input("Enter the second width: "))
secondLength = int(input("Enter the second length: "))

firstRectangle = firstWidth * firstLength

secondRectangle = secondWidth * secondLength

if firstRectangle > secondRectangle:
    print("The area of the first rectangle is larger.")
elif firstRectangle < secondRectangle:
    print("The area of the second rectangle is larger.")
else:
    print("The areas are equals.")
