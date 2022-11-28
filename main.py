### Import required packages. ###

import pandas


### Read .csv-file with morse alphabet. ###

data = pandas.read_csv("morse_alphabet.csv")

### Check if data in file displays correctly. ###
morse_dict = {row.character: row.code for (index, row) in data.iterrows()}
# print(morse_dict)

### Function that asks for input, converts to upper-case and outputs morse. ###


def generate_morse():
    user_input = input("Enter text or characters that need to be converted to morse code. Input can be letters, "
                       "numbers, commas, "
                       "periods and spaces: \n").upper()
    try:
        morse_output = [morse_dict[character] for character in user_input]
    except KeyError:
        print("Sorry. You have used a wrong character.")
        generate_morse()
    else:
        print("\nYour text is converted into the following morse code:\n")
        print(*morse_output, sep="")
        print("\nPlease note that the '/' is used to distinguish between characters and/or to mark the end of the "
              "output. A '//' is used to highlight a space, usually used between words.")


### Call the function. ###

generate_morse()
