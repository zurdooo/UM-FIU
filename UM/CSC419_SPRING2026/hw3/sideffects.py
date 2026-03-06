# Global variables
global_counter = 0
global_list = [0]


def increment_counter():
    global global_counter
    global_counter += 1


def add_to_global_list():
    global global_list
    global_list.append(global_counter)


def main():
    # Before the functions
    print("Before incrementing counter:", global_counter)
    print("Before adding to global list:", global_list)

    increment_counter()
    add_to_global_list()

    # After the functions
    print("After incrementing counter:", global_counter)
    print("After adding to global list:", global_list)


if __name__ == "__main__":
    main()
