
# Resuelvo sin usar pandas

with open("file1.txt") as data1:
    file1_list = [numero.strip() for numero in data1]

with open("file2.txt") as data2:
    file2_list = [numero.strip() for numero in data2]

result = [int(num) for num in file1_list if num in file2_list]
print (result)