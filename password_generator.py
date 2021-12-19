# This will be used as a command line password generator and as a module for
# the functions should I make a GUI version

import random
import string

# Menu options
GENERATE_RANDOM = 1
NEW_PARAMETERS = 2
GENERATE_CUSTOM = 3
QUIT = 4


def main():
    length = 0
    uppercase = 0
    numbers = 0
    special = 0
    choice = 1
    password = ''

    while choice != QUIT:
        choice = display_menu()
        if choice == GENERATE_RANDOM:
            password = random_password()
        elif choice == NEW_PARAMETERS:
            length, uppercase, numbers, special = \
                set_custom_parameters(length, uppercase, numbers, special)
            password = generate_custom(length, uppercase, numbers,
                                       special)
        elif choice == GENERATE_CUSTOM:
            password = generate_custom(length, uppercase, numbers, special)
        print('')
        print('')
        print('')
        print('----------------------------------------------------------')
        print(f'PASSWORD: {password}')
        print('----------------------------------------------------------')
        print('')
        print('')
        print('')


# Create a function that gets password parameters as an input from user
def set_length(length):
    # Ask user if the would like to update the password length
    print(f'The current password length is {length}')
    update = input('Would you like to enter a new length? Y for yes N for '
                   'no: ')
    update = update.lower()

    while update == 'y':
        length = input('Please enter the desired password length: ')

        # Validate the entered password length to force Integer greater than 0
        while length == '0':
            print('Length cannot be 0.')
            length = input('Please enter the desired password length: ')
            # update = 'y'
        try:
            length = int(length)
            break
        except ValueError:
            print('Please enter a valid Integer for Password Length.')

    return length


def set_uppercase(uppercase):
    # Determine if User wants to change number of uppercase characters
    print(f'The current number of uppercase letters is at minimum {uppercase}')
    update = input('Do you need a different number of uppercase letters? Y '
                   'for '
                   'yes N for no: ')
    update = update.lower()

    while update == 'y':
        uppercase = input('Please enter the desired number of uppercase '
                          'letters: ')

        # Validate the entered password length to force Integer greater than 0

        try:
            uppercase = int(uppercase)
            break
        except ValueError:
            print('Please enter a valid Integer for uppercase letters.')

    return uppercase


def set_numbers(numbers):
    # Determine if User wants to change number of uppercase characters
    print(f'The current amount of numbers is at minimum {numbers}')
    update = input('Do you need a different amount of numbers? Y for '
                   'yes N for no: ')
    update = update.lower()

    while update == 'y':
        numbers = input('Please enter the desired amount of numbers: ')

        # Validate the entered password length to force Integer greater than 0

        try:
            numbers = int(numbers)
            break
        except ValueError:
            print('Please enter a valid Integer for the amount of numbers.')

    return numbers


def set_special(special):
    # Determine if User wants to change number of uppercase characters
    print(f'The current number of special characters is at minimum {special}')
    update = input('Do you need a different number of special characters? Y '
                   'for yes N for no: ')
    update = update.lower()

    while update == 'y':
        special = input('Please enter the desired number of special '
                        'characters: ')

        # Validate the entered password length to force Integer greater than 0

        try:
            special = int(special)
            break
        except ValueError:
            print('Please enter a valid Integer for uppercase letters.')

    return special


# Create a function that accepts inputs for password parameters as arguments
def generate_custom(length, uppercase, numbers, special):
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = ''
    # Add required specific characters
    for u in range(uppercase):
        password += random.choice(string.ascii_uppercase)

    for n in range(numbers):
        password += random.choice(string.digits)

    for s in range(special):
        password += random.choice(string.punctuation)

    # Generate other characters
    remaining = length - uppercase - numbers - special
    for r in range(remaining):
        password += random.choice(random_source)

    # Make password a list and shuffle it
    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


def random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = ''

    length = random.randrange(8, 17)

    for x in range(length):
        password += random.choice(random_source)

    return password


def display_menu():
    print('1. Generate a completely random password')
    print('2. Enter custom password parameters')
    print('3. Generate a password using entered parameters')
    print('4. Quit')
    choice = int(input('Please enter your choice: '))
    while choice < 1 or choice > 4:
        choice = int(input('Invalid choice. Please enter a valid menu '
                           'option: '))

    return choice


def set_custom_parameters(length, uppercase, numbers, special):
    length = set_length(length)
    uppercase = set_uppercase(uppercase)
    numbers = set_numbers(numbers)
    special = set_special(special)

    return length, uppercase, numbers, special


if __name__ == '__main__':
    main()
