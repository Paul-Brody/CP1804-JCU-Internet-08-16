'''
This is my first demo test for GIT
'''


def get_user_number_of_items():
    x = 4

    for i in range(0, x):
        print(i)


def catch_their_name():  # get users first name
    print("What is your name? ")
    first = input()
    name = first
    return name


'''Main'''


def main():
    get_user_number_of_items()
    name = catch_their_name()
    print("\n " + "Welcome " + name + "\n")
main()