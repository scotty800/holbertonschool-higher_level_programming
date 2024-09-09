#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in (matrix):
        lenght = len(i)
        for j in range(lenght):
            if j < lenght - 1:
                print("{:d}".format(i[j]), end=" ")
            else:
                print("{:d}".format(i[j]), end="")
        print()
