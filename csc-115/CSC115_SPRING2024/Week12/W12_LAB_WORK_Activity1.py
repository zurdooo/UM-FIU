def main():
    print("WEEK 12 LAB WORK ACTIVITY 1")
    
    #PRINT CONTENTS OF THE FILE
    outFile = open("activity1.txt", "r")
    
    lines = outFile.readlines()
    
    print("-" * 50)
    print('Contents of the file ' + '"activity.1.txt"' + ':')
    print("-" * 50)
    
    for line in lines:
        print(line.rstrip())
    
    outFile.close()
    
    
    print("PROGRAM COMPLETED")

if __name__ == "__main__":
    main()