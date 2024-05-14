# Final Project
import random


class Courses:
    def __init__(self, name, credit_hours, letter_grade):
        self.name = name
        self.credit_hours = credit_hours
        self.letter_grade = letter_grade

    def __str__(self):
        return f"Course: {self.name}, Credit Hours: {self.credit_hours}, Letter Grade: {self.letter_grade}"


class Students:
    def __init__(self, full_name, email, major, project_info):
        self.full_name = full_name
        self.email = email
        self.major = major
        self.project_info = project_info
        self.courses = []
        self.letter_grade_gpa = {
            "A+": 4.0,
            "A": 4.0,
            "A-": 3.7,
            "B+": 3.3,
            "B": 3.0,
            "B-": 2.7,
            "C+": 2.3,
            "C": 2.0,
            "C-": 1.7,
            "D+": 1.3,
            "D": 1.0,
            "F": 0.0,
        }

    def __str__(self):
        return(f"{self.full_name}, {self.email}, {self.major}, {self.project_info}")

    def add_course(self, course):
        # add course to the list
        self.courses.append(course)

    def letter_grade_to_gpa(self, letter_grade):
        return self.letter_grade_gpa[letter_grade]

    def calculate_gpa(self):
        credit_hours = 0
        points = 0
        # loop through the courses and calculate the gpa
        # gpa = sum of (credit hours * gpa of letter grade) / sum of credit hours
        for course in self.courses:
            credit_hours += course.credit_hours
            points += course.credit_hours * self.letter_grade_to_gpa(
                course.letter_grade
            )

        gpa = points / credit_hours
        return f"{gpa:.2f}"

    def print_student_gpa(self):

        for each_course in self.courses:
            print(each_course)

        print("GPA: ", self.calculate_gpa())


# CALCULATE GPA
def calculate_student_gpa():
    student_info = input(
        "Enter full name, email, major, and project information (Separated by commas):"
    )
    student_info_list = student_info.split(",")

    # create a student object from the input
    student = Students(
        student_info_list[0],
        student_info_list[1],
        student_info_list[2],
        student_info_list[3],
    )

    # ask how many courses to enter
    num_courses = input("Enter the number of courses: ")
    # validate the number of courses
    while (
        num_courses.isdigit() == False or int(num_courses) > 6 or int(num_courses) < 2
    ):
        num_courses = input("Invalid Input. Enter the number of courses: ")

    # create a course object for each course
    for each_course in range(int(num_courses)):
        # get the course info
        print(f"For Course {each_course + 1}")
        course_info = input(
            "Enter the course name, credit hours, and letter grade (Separated by commas):"
        )
        course_info_list = course_info.split(",")

        # validate the course info
        course_name = course_info_list[0]
        course_credit_hours = int(course_info_list[1])

        # validate the credit hours
        while course_credit_hours < 1 or course_credit_hours > 4:
            course_credit_hours = int(input("Enter the credit hours (1-4): "))
        course_letter_grade = course_info_list[2]

        # validate the letter grade
        while course_letter_grade not in student.letter_grade_gpa:
            course_letter_grade = input("Enter a valid letter grade: ")

        # add the course to the student
        student.add_course(
            Courses(course_name, course_credit_hours, course_letter_grade)
        )

    print()
    print("Student Information")
    print(student)
    print()

    # call functions to print the student info and gpa
    student.print_student_gpa()
    print()


# LOTTERY
def lottery():
    print("-" * 50)
    print("GENERATE LUCKY NUMBERS")
    print("-" * 50)
    # first five numbers should be in the range of 1-69 no duplicates
    # last number should be in the range of 1-26
    five_ranodm_numbers = []
    while len(five_ranodm_numbers) < 5:
        num = random.randint(1, 69)
        #
        while num in five_ranodm_numbers:
            num = random.randint(1, 69)
        five_ranodm_numbers.append(num)
        #
    # sort the list in ascending order
    five_ranodm_numbers.sort()
    print("Your lottery numbers are: ", *five_ranodm_numbers)
    # get the last number then append it to the list
    last_num = random.randint(1, 26)
    print("Your Powerball number is: ", last_num)
    five_ranodm_numbers.append(last_num)
    # print the list without the brackets
    print("Here is the final: ", *five_ranodm_numbers)


# PIG LATIN
def pig_latin():
    print("-" * 50)
    print("GENERATE PIG LATIN")
    print("-" * 50)
    sentence = input("Enter sentence to be converted into Pig Latin: ")
    # split the sentence into a list of words
    list_of_words = sentence.split()
    # empty string to store the new sentence in pig latin
    new_sentence = ""
    # loop through the list and convert them to pig latin add a spcae at the end
    for word in list_of_words:
        new_sentence += (word[1:].upper() + word[0].upper() + "AY") + " "
    print(new_sentence)


# ROCK PAPER SCISSORS
# FIX
def rock_paper_scissors():
    print("-" * 50)
    print("GENERATE LUCKY NUMBERS")
    print("-" * 50)
    # Computer chooses 1 for rock, 2 for paper, 3 for scissors
    computer_choice = random.randint(1, 3)
    # User input
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ")
    # validate user input
    while (
        user_choice != "rock" and user_choice != "paper" and user_choice != "scissors"
    ):
        user_choice = input("Invalid input. Enter 'rock', 'paper', or 'scissors': ")
    if computer_choice == 1:
        print("Player's Choice:", user_choice)
        print(f"Computer chose: 'rock'")
    elif computer_choice == 2:
        print("Player's Choice:", user_choice)
        print(f"Computer chose: 'paper'")
    elif computer_choice == 3:
        print("Player's Choice:", user_choice)
        print(f"Computer chose: 'scissors'")
    # rock choices
    if user_choice == "rock" and computer_choice == 1:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == 2:
        print("Computer wins!")
    elif user_choice == "rock" and computer_choice == 3:
        print("You win!")
    # paper choices
    elif user_choice == "paper" and computer_choice == 1:
        print("You win!")
    elif user_choice == "paper" and computer_choice == 2:
        print("It's a tie!")
    elif user_choice == "paper" and computer_choice == 3:
        print("Computer wins!")
    # scissors choices
    elif user_choice == "scissors" and computer_choice == 1:
        print("Computer wins!")
    elif user_choice == "scissors" and computer_choice == 2:
        print("You win!")
    elif user_choice == "scissors" and computer_choice == 3:
        print("It's a tie!")


# main function call
def main():
    print("Welcome to the CSC115 final project.")
    # main menu loop
    menu = (
        "Enter 1 to calculate GPA"
        "\nEnter 2 for Lottery Number Generator"
        "\nEnter 3 for Pig Latin"
        "\nEnter 4 for Rock, Paper, Scissors"
        "\nEnter 9 to exit"
    )
    print(menu)

    # user input
    user_input = input("Enter menu option 1, 2, 3, 4, or 9 to exit: ")

    # while not 9 else exit the program
    while user_input != "9":
        if user_input == "1":
            calculate_student_gpa()
        elif user_input == "2":
            # lottery
            lottery()
        elif user_input == "3":
            # pig latin
            pig_latin()
        elif user_input == "4":
            # rock paper scissors
            rock_paper_scissors()
        else:
            # invalid menu option
            print("Invalid Option")

        # restart the menu
        print("-" * 50)
        print(menu)
        user_input = input("Enter menu option 1, 2, 3, 4, or 9 to exit: ")

    print("You have exited the program. Goodbye.")


if __name__ == "__main__":
    main()
