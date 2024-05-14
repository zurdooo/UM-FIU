def main():
    print("WEEK 12 LAB WORK ACTIVITY 1")

    file_name = input("Enter the name of the file: ")

    # WRITE TO FILE
    outFile = open(file_name, "w")

    number_exam_scores = int(input("Enter the number of exams: "))

    for exam_num in range(number_exam_scores):
        exam_score = input(f"Enter the exam score for exam {exam_num + 1}: ")
        outFile.write(str(exam_score) + "\n")

    outFile.close()

    # READ FROM FILE
    inFile = open(file_name, "r")

    print("-" * 50)
    print("Contents of the file: " + file_name + ":")
    print("-" * 50)

    exam_count = 0
    total_score = 0

    for line in inFile:
        print(f"Exam {exam_count}: {line.rstrip()}")
        total_score += int(line)

        exam_count += 1

    average_score = total_score / exam_count
    print(f"Average: {average_score}")

    if average_score >= 90:
        final_letter_grade = "A"
    elif average_score >= 80:
        final_letter_grade = "B"
    elif average_score >= 70:
        final_letter_grade = "C"
    elif average_score >= 60:
        final_letter_grade = "D"
    else:
        final_letter_grade = "F"

    inFile.close()
    
    print(final_letter_grade)

    # APPEND TO FILE
    outFile = open(file_name, "a")
    
    outFile.write(f"Average: {average_score}\n")
    outFile.write(f"Final Grade: {final_letter_grade}\n")
    
    outFile.close()

    print("PROGRAM COMPLETED")


if __name__ == "__main__":
    main()
