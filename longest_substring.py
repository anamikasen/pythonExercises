import numpy as np

string1 = input("Enter string 1 ")
string2 = input("Enter string 2 ")

sim_matrix = [[0 for x in range(len(string1))] for y in range(len(string2))]

for i, letter_2 in enumerate(string2):
    for j, letter_1 in enumerate(string1):
        if letter_1==letter_2:
            if sim_matrix[i-1][j-1] is not None:
                sim_matrix[i][j] = sim_matrix[i-1][j-1] + 1
            else:
                sim_matrix[i][j] = 1
print(sim_matrix)
