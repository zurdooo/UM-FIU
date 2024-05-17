print("WEEK 10 - LAB ACTIVITY 1")

KILOMETERS_TO_MILES = 0.621


def showMiles(kilometers):
    miles = kilometers * KILOMETERS_TO_MILES
    print(f"The conversion of {kilometers} kilometers to miles is {miles} miles")


def main():
    kilometers = float(input("Enter the number of kilometers: "))
    showMiles(kilometers)


main()
