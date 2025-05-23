import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict_1= {row.letter: row.code for (index, row) in data.iterrows()}

# print(dict_1)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What's your name?").upper()
code_word_list = [(dict_1[letter]) for letter in name]

print (code_word_list)
