def practice3():
    
    student_name_list = ["Maria Fernandez", "Alex Ramos", "Hien Nguyen"]
    
    student_exam_list = []
    
    for student in student_name_list:
        
        exam_score = float(input(f"Enter the exam score for {student}: "))
        while exam_score < 0  or exam_score > 100:
            exam_score = float(input(f"Invalid Input. Re-Enter the exam score for {student}: "))
        
        student_exam_list.append(exam_score)
    
    print(student_name_list)
    print(student_exam_list)

def practice2():
    print("-" * 50)
    print("WEEK 13 LAB PRACTICE 2")
    print("-" * 50)

    my_grade = "100,90,80"

    print(my_grade)

    my_grade_list = my_grade.split(",")
    print(my_grade_list)

    my_grade_list_total = 0
    for grade in my_grade_list:
        my_grade_list_total += int(grade)
    
    print(my_grade_list_total)

    average = my_grade_list_total / len(my_grade_list)
    
    print(f"The average is: {average}")

def practice1():
    print("-" * 50)
    print("WEEK 13 LAB PRACTICE 1")
    print("-" * 50)

    school_name = "University of Miami"
    print(school_name)

    school_name_list = school_name.split()
    print(school_name_list)

    print(school_name_list[0])
    print(school_name_list[0][0])


# ----------------------------------------------------------
def main():
    print("CSC115 - WEEK 13  - LAB PRACTICE")
    practice3()


if __name__ == "__main__":
    main()
