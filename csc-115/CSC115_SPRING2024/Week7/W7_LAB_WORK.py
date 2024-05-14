print("Activity 1:")
print("This program displays the square and square root of a number")

first_number = int(input("Enter first number in range: "))
second_number = int(input("Enter second number in range: "))

while first_number > second_number:
    second_number = int(
        input("Invalid Input. Please Re-etner the second number in the range: ")
    )

print("Number \t SquareRoot \t Squared")
print("-" * 32)

for number in range(first_number, second_number + 1):
    if number < 0:
        print(f"{number} \t N/A(Negative) \t {number ** 2}")
    else:
        print(f"{number} \t {number ** 0.5:.2f} \t\t {number ** 2}")


print('Activity 2')

amount_students = int(input('How many students do you have '))
while(amount_students > 5 or amount_students < 0):
    print('Invalid input. Please enter a posotive integer number between 1 - 5 only ')
    amount_students = int(input('How many students do you have '))

testscore_per_student = int(input('How many test scors per student do you have '))
while testscore_per_student < 1 or testscore_per_student > 3:
    print('Invalid input. Please enter a posotive integer number between 1 - 3 only ')
    testscore_per_student = int(input('How many test scors per student do you have '))

print()
print('-' * 30)
print('Number of students',amount_students)
print('Number of tests per student', testscore_per_student)
print('-' * 30)
print()

for student in range(1, amount_students + 1):
    averagesum = 0
    print('Student Number', student)
    print('-' * 30)
    for score in range(1, testscore_per_student + 1):
        current_score = int(input(f'Test score # {score}: '))
        while current_score < 0 or current_score > 100:
            print('Invalid score. Please re-enter the real number between 0 - 100')
            current_score = int(input(f'Test score # {score}: '))
        averagesum += current_score
    print(f'The average for student number {student} is : {averagesum/testscore_per_student}')
    print()

