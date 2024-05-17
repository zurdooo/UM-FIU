print("WEEK 6 - LAB WORK")

print("Activity 1")

exam1 = int(input("Enter exam 1 score: "))
while exam1 < 0 or exam1 > 100:
    exam1 = int(input("Invalid input. Enter exam 1 score between 0 - 100: "))
exam2 = int(input("Enter exam 2 score: "))
while exam2 < 0 or exam2 > 100:
    exam2 = int(input("Invalid input. Enter exam 2 score between 0 - 100: "))
exam3 = int(input("Enter exam 3 score: "))
while exam3 < 0 or exam3 > 100:
    exam3 = int(input("Invalid input. Enter exam 3 score between 0 - 100: "))

examScore = [exam1, exam2, exam3]
averagescore = sum(examScore) / len(examScore)

count = 1

for i in examScore:
    print(f"Exam {count}: {i}")
    count += 1
print(f"Average = {averagescore}")

print('The exam score and average result:')

if averagescore >= 90:
    print("Your final  grade is: A")
elif averagescore >= 80:
    print("Your final grade is: B")
elif averagescore >= 70:
    print("Your final  grade is: C")
elif averagescore >= 60:
    print("Your final  grade is: D")
else:
    print("Your final  grade is: F")

print("Activity 2")

print('Welcome to my Python Calculator Program')

menu = ('Press 1 to ADD'
        '\nPress 2 to SUBTRACT'
        '\nPress 3 to MULTIPLY'
        '\nPress 4 to DIVIDE'
        '\nPress 9 to EXIT')

print(menu)

user_input = int(input('Enter 1 of the 5 choices from the menu: '))
while(user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input != 9):
    user_input = int(input('Invalid input. Enter 1 of the 5 choices from the menu: '))

print('User selected option', user_input)

while(user_input != 9):
    if user_input == 1:
        print('Perform ADDITION operator')
        print('.........................')
    elif user_input == 2:
        print('Perform ADDITION operator')
        print('.........................')
    elif user_input == 3:
        print('Perform ADDITION operator')
        print('.........................')
    elif user_input == 4:
        print('Perform ADDITION operator')
        print('.........................')
    

    print(menu)
    user_input = int(input('Enter 1 of the 5 choices from the menu: '))
    while(user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input != 9):
        user_input = int(input('Invalid input. Enter 1 of the 5 choices from the menu: '))
print('User selected option', user_input)
print('REACHED END OF PROGRAM')