#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    for i in range(rows):
        columns = len(matrix[i])
        for j in range(columns):
            if j != columns -1:
                separator = ' '
            else:
                separatoer = ''
            print("{:d}".format(matrix[i][j]), end =separator)
        print("")
