# 3D Matrix finding the longest string

# creating empty matrix
import numpy as np
def createEmptyMat():
    empty_matrix = np.zeros((7,5,3))
    # for layer in empty_matrix:
    #   for row in layer:
    #       print(row)
    #   print()
    return empty_matrix


# Inserting new values in matrix
def update_matrix(matrix):
    # Iterate over each element in the 3D matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                # Calculate the sum of the indices
                index_sum = i + j + k

                # Assign value based on whether the index sum is odd or even
                if (index_sum % 10 == 2 or index_sum % 10 == 4):
                    matrix[i][j][k] = 0
                else:
                    matrix[i][j][k] = 1
    return matrix


# finding the longest substrring of one
def find_longest_substring(matrix):
    largest, coordinates = 0, []

    def check_line(line):
        nonlocal largest, coordinates
        count, temp = 0, []
        for pos in line:
            if pos[0] == 1:
                count += 1
                temp.append(pos[1])
            else:
                if count > largest:
                    largest, coordinates = count, temp[:]
                count, temp = 0, []
        if count > largest:
            largest, coordinates = count, temp[:]

    for d in range(7):
        for r in range(5):
            check_line([(matrix[d][r][c], [d,r,c]) for c in range(3)])
        for c in range(3):
            check_line([(matrix[d][r][c], [d,r,c]) for r in range(5)])

    for r in range(5):
        for c in range(3):
            check_line([(matrix[d][r][c], [d,r,c]) for d in range(7)])

    print(f"Largest contiguous subarray of 1s: {largest}")
    print("Coordinates:", coordinates)


# main function
def main():
    # print("Empty Matrix:")
    matrix = createEmptyMat()
    print("Updated Matrix:")
    matrix = update_matrix(matrix)
    for layer in matrix:
      for row in layer:
          print(row)
      print()
    find_longest_substring(matrix)

main()