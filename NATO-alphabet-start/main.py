# student_dict = {
    # "student": ["Angela", "James", "Lily"],
    # "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#--------------------------------------------------------------------------------------

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {title.letter:title.code for (index, title) in df.iterrows()}

while True:
    user_input = input("Enter the name: ")

    chars = [char.upper() for char in user_input]
    nato_list = [nato_dict[letter] for letter in chars]
    print(nato_list)




