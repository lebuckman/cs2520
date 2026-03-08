"""
Write a function that converts a given 2D list (a list of lists) into a 1D list. 
The function return the 1D list
"""


def convert_2D_to_1D(two_d_list):
    one_d_list = []
    for sublist in two_d_list:
        one_d_list.extend(sublist)
    return one_d_list


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(convert_2D_to_1D(matrix))
