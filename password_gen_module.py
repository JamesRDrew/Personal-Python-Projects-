# This will be used as a module that contains functions for the password
# generator command line and GUI programs

# Create a function that getrs password perameters as an input from user
def set_length(length):

    # Ask user if the would like to update the password length
    # FIGURE OUT WHY TRY BLOCK ONLY RUNS ONCE 

    print(f'The current password length is {length}')
    update = input('Would you like to enter a new length? Y for yes N for no:')
    update = update.lower()

    if update == 'y':

        # Validate the entered password length to force Integer greater than 0
        try:
            length = int(input('Please enter the desired password length: '))
        except ValueError:
            length = int(input('Please enter a valid integer for password '
                               'length: '))
        while length == 0:
            print('Length cannot be 0.')
            length = int(input('Please enter a valid integer for password '
                               'length: '))
    return length









# Create a function that accepts inputs for password parameters as arguments
def password(length, uppercase, lowercase, special)



