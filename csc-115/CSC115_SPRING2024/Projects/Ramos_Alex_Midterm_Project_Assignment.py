# Midterm Project

print("Alex Ramos")
print("axr2714@miami.edu")
print("CSC 115")
print("Biomedical Engineering")

print()
print("This python program displays Roman Numerals and Predicts Population")

# menu
menu = (
    "Enter option 1 to display Roman Numerals"
    "\nEnter option 2 to display Predicts Population"
    "\nEnter 9 to exit"
)
print(menu)

# user input
user_input = input("Please enter a choice 1, 2, or 9: ")

# while not 9 else exit the program
while user_input != "9":
    # roman
    if user_input == "1":
        print()
        print("Here is the ROMAN NUMERALS")
        # valid roman check first
        number_roman = int(input("Enter a number between 1 to 10 only: "))
        while number_roman <= 1 and number_roman >= 10:
            number_roman = int(input("Invalid Option. Please ReEnter a number 1 - 10"))
        # prints the roman numeral by its dictionary key and value
        roman_dict = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
        }
        # prints the roman numeral
        print(
            "Number:",
            number_roman,
            "--------->",
            roman_dict[number_roman],
            "(in Roman Numerals.)",
        )

    # population
    elif user_input == "2":
        print()
        print("Here is the POPULATION")
        # valid starting organism check
        organsims = int(input("Starting number of organisms: "))
        while organsims < 0:
            organsims = int(
                input(
                    "Invalid Input. Please re-enter the number of Starting Organisms: "
                )
            )

        # valid daily increase check
        daily_increase = int(input("Average daily increase: "))
        while daily_increase < 1 or daily_increase > 100:
            daily_increase = int(
                input(
                    "Invalid Input. Please re-enter the Average Daily Increase Input: "
                )
            )

        # valid number of days check
        number_days = int(input("Number of days to multiply: "))
        while number_days < 2 or number_days > 30:
            number_days = int(
                input("Invalid Input. Please re-enter the number of days to multiply: ")
            )

        # loop for every day and print
        for day in range(1, number_days + 1):
            print("Day", day, ":", organsims)
            organsims = organsims + organsims * daily_increase / 100

    # invalid menu option
    else:
        print("Invalid Option")

    # restart the menu
    print()
    print(menu)
    user_input = input("Please enter a choice 1, 2, or 9: ")

#extied loop ended program
print()
print("You just selected option 9 which exits the program. Goodbye.")
print("REACHED END OF PROGRAM")
