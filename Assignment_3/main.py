from read_write import *
from multiply import *

def main():
    filemat1 = "mat1.csv"
    filemat2 = "mat2.csv"
    outputfile = "output.csv"
    mat1 = reading_matrix_from_csv(filemat1)

    print("\nMatrix 1\n")
    for row in mat1:
        print(row)
    mat2 = reading_matrix_from_csv(filemat2)
    print("\nMatrix 2\n")
    for row in mat2:
        print(row)

    print("\nMultiplying Matrix 1 and Matrix 2")
    output = multiplying_matrix(mat1, mat2)

    print("\nThis is the output:\n")
    for row in output:
        print(row)

    storing_in_csv(outputfile, output)

main()