def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
# creates and prints the menu


def encoder(password):
    encoded_password = " "  # created an empty string for a list
    for x in password:
        temp_pass = int(x)
        temp_pass = int(temp_pass + 3) % 10
        encoded_password = encoded_password + str(temp_pass)
    return encoded_password


if __name__ == '__main__':
    # prints menu and asks for input in a loop
    while True:
        # function that prints menu
        print_menu()
        option = int(input("\nPlease enter an option: "))   # asks user for option input
        if option == 1:
            password = input("Please enter your password to encode: ")  # asks user for password to input
            print("Your password has been encoded and stored!\n")
            print(encoder(password))
        elif option == 2:
            password = input("Please enter your password to decode: ")
            print("The encoded password is, and the original password is \n")
        elif option == 3:
            break
