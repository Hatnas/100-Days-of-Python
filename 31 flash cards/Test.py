
import pandas
import random

data = pandas.read_csv("data/french_words.csv")
french_list = data.French.to_list()

data2 = pandas.read_csv("Words_to_learn.csv")
french_list2 = data2.French.to_list()

print(len(french_list))
print(len(french_list2))
