def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
# creates and prints the menu


def password_encode(password):
    # adds 3 to the original password
    encoded_password = "".join([str((int(digit) + 3) % 10) for digit in password])
    return encoded_password

    '''
    encoded_password = " "  # created an empty string for a list
    for x in password:
        temp_pass = int(x)
        temp_pass = int(temp_pass + 3) % 10
        encoded_password = encoded_password + str(temp_pass)
    return encoded_password
    '''

def decoder(password):
    decoded_password = " "
    for x in password:
        temp_pass = int(x)
        temp_pass = int(temp_pass - 3) % 10
        encoded_password = decoded_password + str(temp_pass)
    return decoded_password

if __name__ == '__main__':
    # prints menu and asks for input in a loop
    encoded_password = " "
    password = " "
    while True:
        # function that prints menu
        print_menu()
        option = int(input("\nPlease enter an option: "))   # asks user for option input
        if option == 1:
            password = input("Please enter your password to encode: ")  # asks user for password to input
            print("Your password has been encoded and stored!\n")
            # Removed this because this option only needs to store the password not print it
            # print(password_encode(password))
            encoded_password = password_encode(password)
        elif option == 2:
            # removed this because you only need one password input
            # password = input("Please enter your password to decode: ")
            print(f"The encoded password is {encoded_password}, and the original password is {password} \n")
        elif option == 3:
            break
