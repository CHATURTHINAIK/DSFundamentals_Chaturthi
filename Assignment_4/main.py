def readName(lines):
    f = open("names.csv", 'r')
    lines.append(f.read())

def loadIntoMatrix(lines,mat):
    for line in lines:
        names = line.strip().split('\n')
        mat.extend(names)

def convertToColumnMajor(mat):
    transpose = []
    n = max([len(i) for i in mat])
    for i in range(n):
        temp = ""
        for j in range(len(mat)):
            try:
                temp += mat[j][i]
            except Exception as e:
                temp += " "
        transpose.append(temp.rstrip())
    mat.clear()
    mat.extend(transpose)

def calculateCharacterLength(mat):
    res = 0
    for row in mat:
        res += len(row)
    print(res)

def storeListAsString(mat):
    with open("output.txt","w") as file:
        for i in mat:
            file.write(i)

def main():
    lines = []
    mat = []
    readName(lines)
    loadIntoMatrix(lines,mat)
    print("load matrix:",mat)
    convertToColumnMajor(mat)
    print("Column major:",mat)
    calculateCharacterLength(mat)
    storeListAsString(mat)

main()