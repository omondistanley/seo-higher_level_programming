#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    matrix = []
    for i in range(rows):
        columns = len(matrix[i])
        a = []
        for j in range(columns):
            k = int(input())
            a.append(k)
        matrix.append(a)
    for i in range(rows):
        for j in range(columns):
            print("{:d}{:d}".format(matrix[i][j]), sep=" ")
