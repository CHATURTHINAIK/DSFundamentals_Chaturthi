def reading_matrix_from_csv(filepath):
    f = open(filepath, 'r')
    matrix = []
    for line in f:
        row = line.strip().split(',')
        row = [int(value) for value in row]
        matrix.append(row)
    return matrix

def storing_in_csv(outputfile, output):
    file = open(outputfile, 'w')
    for row in output:
        row_string = ','.join(map(str, row))
        file.write(row_string+'\n')
    print(f"\nOutput stored in output.csv\n")