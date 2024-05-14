print('WEEK 10 - LAB PRACTICE')

def show_message():
    print('Hello World!')
    print('Welcome to  Python Programming')
    print("-" * 20)

def show_another_message(name, major):
    print(f'Name: {name}')
    print(f'Major: {major}')
    print("-" * 20)

def get_name():
    name = input("Enter your name: ")
    return name
def get_major():
    major = input("Enter your major: ")
    return major

#----------------------------------------------------------------------
def main():
    #show_message()

    show_another_message(get_name(), get_major())

main()