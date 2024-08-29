def multiplying_matrix(mat1, mat2):
    mat_1 = mat1
    mat_2 = mat2

    rows = 3
    cols = 3
    cols2 = 3

    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    for r in range(rows):
        for c in range(cols):
            for c1 in range(cols2):
                result[r][c] += mat_1[r][c1] * mat_2[c1][c]
    return result