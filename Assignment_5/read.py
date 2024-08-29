def read_file(filepath):
    file = open(filepath, 'r')
    header = file.readline().strip().split(',')
    data = []
    for line in file:
        row = line.strip().split(',')
        data.append(row)
    return data