def showInitials():

    print("-" * 50)
    print("WEEK 13 LAB ACTIVITY 1: Initials")
    print("-" * 50)

    full_name = input("Enter your full name: ").upper()

    full_name_list = full_name.split()

    for name in full_name_list:
        print(f"{name[0]}. ", end="")


def showSum():

    print("-" * 50)
    print("WEEK 13 LAB ACTIVITY 2: Sum of Digits in a String")
    print("-" * 50)

    sequence = input("Enter a sequence of digits with nothing seperating them: ")

    total_sum = 0

    for digit in sequence:
        total_sum += int(digit)

    print(f"The total value the digits in the string you entered is: {total_sum}")


def showDate():

    print("-" * 50)
    print("WEEK 13 LAB ACTIVITY 3: Date printer")
    print("-" * 50)

    user_date = input("Enter a date in the format mm/dd/yyyy: ")

    while len(user_date) != 10:
        user_date = input(
            "Invalid Format. Please Re-enter a date in the format mm/dd/yyy: "
        )

    date_list = user_date.split("/")

    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    date_list[0] = month_list[int(date_list[0])]

    print(*date_list)


def weeklySales():

    print("-" * 50)
    print("WEEK 13 LAB ACTIVITY 4: Total Sales")
    print("-" * 50)

    day_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    weekly_sales = []

    for day in day_week:
        sales = float(input(f"Enter the sales for {day}: "))
        weekly_sales.append(sales)

    print(f"Total sales for the week: ${sum(weekly_sales):.2f}")


def yearlyRainfall():

    print("-" * 50)
    print("WEEK 13 LAB ACTIVITY 5: Rainfall Statistics")
    print("-" * 50)

    months_year = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    total_rainfall = []

    for month in months_year:
        rainfall = float(input(f"Enter the rainfall for {month}: "))
        total_rainfall.append(rainfall)

    print(f"Total rainfall: {sum(total_rainfall):.2f}")

    average = sum(total_rainfall) / len(months_year)

    print(f"Average rainfall: {average:.2f}")

    highest_value = max(total_rainfall)
    highest_value_index = total_rainfall.index(highest_value)

    print(f"Highest rainfall:  { months_year[highest_value_index]} ")

    lowest_value = min(total_rainfall)
    lowest_value_index = total_rainfall.index(lowest_value)

    print(f"Lowest rainfall:  {months_year[lowest_value_index]}")


def studentsAverages():

    print("-" * 50)
    print("WEEK 13 LAB ACTIVITY 6: Grade Book")
    print("-" * 50)

    student_name_exam_dictionary = {}

    number_students = int(input("Enter the number of students (between 1 - 5 only): "))
    while number_students < 1 or number_students > 5:
        number_students = int(input("Invalid input. Re-enter the number of students: "))

    for each_student_iteration in range(number_students):

        student_name = input(f"Enter student #{each_student_iteration + 1} name: ")

        number_of_exams = int(
            input(f"How many exams does {student_name} have? (between 1-3 only) ")
        )
        while number_of_exams < 1 or number_of_exams > 3:
            number_of_exams = int(
                input(
                    f"Invalid input. How many exams does {student_name} have? (between 1-3 only) "
                )
            )

        student_exam_scores = []
        for exam_score_iteration in range(number_of_exams):
            exam_score = float(input(f"Enter exam {exam_score_iteration + 1}: "))
            student_exam_scores.append(exam_score)

        student_name_exam_dictionary[student_name] = student_exam_scores

    print(student_name_exam_dictionary)

    for student_name in student_name_exam_dictionary:

        length_exams = len(student_name_exam_dictionary[student_name])
        student_exam_average = (
            sum(student_name_exam_dictionary[student_name]) / length_exams
        )

        print(
            f"{student_name} has {length_exams} exams and the average is {student_exam_average}"
        )


# ----------------------------------------------------------
def main():
    print("CSC115 - WEEK 13 LAB WORK")

    # Activity 1
    # showInitials()

    # Activity 2
    # showSum()

    # Activity 3
    # showDate()

    # Activity 4
    # weeklySales()

    # Activity 5
    # yearlyRainfall()

    # Activity 6
    studentsAverages()


if __name__ == "__main__":
    main()
