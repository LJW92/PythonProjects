# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

import pandas

data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
print(nato_dict)


# TODO 1. Create a dictionary in this format:
# var = {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Enter a word: ")
    try:
        result = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print('Sorry, Only letters in the alphabet please')
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
