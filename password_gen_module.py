# This will be used as a command line password generator and as a module for
# the functions should I make a GUI version

import random
import string


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
    print(f'The current number of uppercase letters is {uppercase}')
    update = input('Do you need a different number of upercase letters? Y for '
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
    print(f'The current amount of numbers is {numbers}')
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
    print(f'The current number of special characters is {special}')
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
def create_password(length, uppercase, numbers, special):
    none

def main():
    length = 0
    uppercase = 0
    numbers = 0
    special = 0

    length = set_length(length)
    uppercase = set_uppercase(uppercase)
    numbers = set_numbers(numbers)
    special = set_special(special)

    print(length)
    print(uppercase)
    print(numbers)
    print(special)

if __name__ == '__main__':
    main()







