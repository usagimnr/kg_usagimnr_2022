# Author: Madeline Rodriguez
# Program Description: This program will determine if two strings 
# can be mapped one-to-one. For this program I used the definition
# of a one-to-one function which means every distinctive value of 
# the first string has to map to a value of the second string but
# not every value of the second string has to be paired with one of
# the first. Also a character in the first string cannot map two 
# different characters.

import sys

# Main function will take in two inputs as arguments and assigns the 
# inputs as strings. These string will be the arugments of the function 
# OneToOne.
def main():
    if len(sys.argv) > 2:
        s1 = str((sys.argv[1]))
        s2 = str((sys.argv[2]))
    # If no arguments or only one input is given an error message
    # will display
    else:
        sys.exit('Error - Invalid input')

    print(OneToOne(s1, s2))

# OneToOne function will evaluate whether there exists a one-to-to
# character mapping between the two strings. 
def OneToOne(a, b):
    #If the length of a is greater than b it cannot be one-to-one
    if len(a) > len(b):
        return False

    # This dictionary will keep track of which characters are being 
    # mapped as it loops through each character in the first string
    dictMap = {}
    for i in range(len(a)):
        # If a character in string a is not in the dictionary it will 
        # be mapped with its corresponding character in string b
        if a[i] not in dictMap:
            dictMap[a[i]] = b[i]
        # If the character in string a is already in the dictionary
        # this checks if the value matches that of the dictionary
        elif dictMap[a[i]] == b[i]:
            return True
        # If it is a different value them this is not a one-to-one 
        # mapping since one character in string one cannot map more
        # than one character
        else:
            return False
    return True
   
main()