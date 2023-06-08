#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = int(input('Enter the number of rows'))
    columns = int(input('Enter the number of columns'))
    matrix = []
    for i in range(rows):
        a = []
        for j in range(columns):
            k = int(input())
            a.append(k)
        matrix.append(a)
    for i in range(rows):
        for j in range(columns):
            print("{}{}".format(matrix[i][i]), sep=" ")
