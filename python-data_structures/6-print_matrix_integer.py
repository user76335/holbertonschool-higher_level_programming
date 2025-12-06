
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            end = " " if i < len(row) - 1 else ""
            print("{:d}".format(row[i]), end=end)
        print()
