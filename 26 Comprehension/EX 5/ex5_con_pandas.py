import pandas as pd

# Tengo que crear una lista (results) con los elementos que esten en los dos txt

# Defino que no tiene header por lo que no toma el primer valor como header
data1 = pd.read_csv("file1.txt", header=None)

data2 = pd.read_csv("file2.txt", header=None)

file1_list = data1[0].to_list()
file2_list = data2[0].to_list()

# otra forma de hacerlo con List Comprehension es:
# file1_list =[ num for num in data1[0]]
# file2_list =[ num for num in data2[0]]

result = [num for num in file1_list if num in file2_list]

print (result)

