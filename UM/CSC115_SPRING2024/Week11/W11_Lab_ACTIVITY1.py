def get_name():
    name = input("Enter your name: ")
    return name


# --------------------------------------


def get_major():
    major = input("Enter your major: ")
    return major


# --------------------------------------


def get_gpa():
    gpa = float(input("Enter your gpa: "))
    return gpa


# --------------------------------------


def get_contact_email():
    contact_email = input("Enter your contact email: ")
    return contact_email


# --------------------------------------


def is_score_valid(aScore):
    if aScore >= 0.0 and aScore <= 100.0:
        return True
    else:
        return False


# --------------------------------------


def get_an_exam_score():
    exam_score = float(input("Enter an exam score: "))
    while not is_score_valid(exam_score):
        exam_score = float(input("Invalid input. Enter an exam score: "))
    return exam_score


# --------------------------------------


def get_average(scores):
    average = sum(scores) / len(scores)
    return average


# --------------------------------------


def get_letter_grade(aScore):
    if aScore >= 90:
        return "A"
    elif aScore >= 80:
        return "B"
    elif aScore >= 70:
        return "C"
    elif aScore >= 60:
        return "D"
    else:
        return "F"


# --------------------------------------


def get_average_and_letter_grade(scores):
    average = get_average(scores)
    letter_grade = get_letter_grade(average)
    return average, letter_grade


# --------------------------------------


def get_exam_scores_list():

    number_of_exams = int(input("Enter the amount of exam scores: (1-5) "))
    while number_of_exams < 1 or number_of_exams > 5:
        number_of_exams = int(
            input("Invalid input. Enter the amount of exam scores: (1-5) ")
        )

    exam_list = []
    for exam in range(1, number_of_exams + 1):
        print(f"Enter exam {exam} score: ")
        exam = get_an_exam_score()
        exam_list.append(exam)

    return exam_list


# --------------------------------------


def show_student_info_and_grades(
    name, major, gpa, email, scores, aveerage, letterGrade
):
    print("-" * 50)
    print(f"Student Name: {name}")
    print(f"Student Major: {major}")
    print(f"Student GPA: {gpa}")
    print(f"Student Email: {email}")
    print(f"Studen exam Scores: {scores}")
    print(f"The average is: {aveerage:.2f}. THe final letter grade is: {letterGrade}")
    print("-" * 50)


# --------------------------------------


def main():
    student_name = get_name()
    student_major = get_major()
    student_GPA = get_gpa()
    student_email = get_contact_email()
    student_exams_list = get_exam_scores_list()
    average_score, final_letter_grade = get_average_and_letter_grade(student_exams_list)

    show_student_info_and_grades(
        student_name,
        student_major,
        student_GPA,
        student_email,
        student_exams_list,
        average_score,
        final_letter_grade,)


if __name__ == "__main__":
    main()
