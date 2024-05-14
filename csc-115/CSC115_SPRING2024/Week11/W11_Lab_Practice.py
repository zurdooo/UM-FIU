def is_even_number(anumber):
    if anumber % 2 == 0:
        return True
    else:
        return False


def get_a_number():
    input_number = int(input("Enter a number: "))
    return input_number


# --------------------------------------
import random


def get_a_random_number():
    return random.randint(10, 100)


def main():
    print("WEEK 11 - LAB PRACTICE")
    print("-" * 50)

    input_number = get_a_number()
    if is_even_number(input_number):
        print(f"The number {input_number} is EVEN.")
    else:
        print(f"The number {input_number} is ODD.")


if __name__ == "__main__":
    main()
main()
