import random


def main():
    print("WEEK 12 LAB WORK ACTIVITY 1")

    file_name = input("Enter the name of the file: ")

    # WRITE TO FILE
    outFile = open(file_name, "w")

    number_of_random_numbers = int(input("Enter the number of random numbers: "))

    for _ in range(number_of_random_numbers):
        random_number = random.randint(1, 100)
        outFile.write(str(random_number) + "\n")

    outFile.close()

    # READ FROM FILE
    inFile = open(file_name, "r")

    print("-" * 50)
    print("Contents of the file" + file_name + ":")
    print("-" * 50)

    lines = inFile.readlines()
    for line in lines:
        print(line.rstrip())

    inFile.close()

    print("PROGRAM COMPLETED")


if __name__ == "__main__":
    main()
