def main():
    infile = open("exam.txt", "r")
    
    total_lines_list = infile.readlines()
    number_of_exams = len(total_lines_list)
    total_points = 0
    for line in total_lines_list:
        exam_score = float(line.rstrip("\n"))
        total_points += exam_score
        print(f"Exam score: {exam_score:.2f}")
    
    average_score = total_points / number_of_exams
    print(f"Average score: {average_score:.2f}")
    
    infile.close()
    
if __name__ == "__main__":
    main()