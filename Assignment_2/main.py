import matplotlib.pyplot as plt

def read_file(filepath):
    f = open(filepath, "r")
    lines = f.readlines()
    return lines

def read_header(lines):
    if not lines:
        print("File is empty")
        return None
    else:
        header = lines[0].strip().split(',')
        return header

# Gender Pie Chart
def count_gender(header, lines):
    if 'Gender' not in header:
        print("Gender column is missing")
    else:
        data = [line.strip().split(',') for line in lines[1:]]

    gender_index = header.index('Gender')
    male = 0
    female = 0
    for row in data:
        if len(row) > gender_index:
            if row[gender_index] == 'Male':
                male = male + 1
            elif row[gender_index] == 'Female':
                female = female + 1
            else:
                pass
        else:
            print("Row is missing")
    gen = [male, female]
    return gen

# Subject Pie Chart

# For Maths
def count_math_result(header, lines):
    if 'MathMarks' not in header:
        print('MathMarks column is missing')
    else:
        data = [line.strip().split(',') for line in lines[1:]]

    mathmark = header.index('MathMarks')
    passed = 0
    failed = 0
    for row in data:
        if len(row) > mathmark:
            mk = int(row[mathmark])
            if mk < 40:
                failed = failed + 1
            else:
                passed = passed + 1
        else:
            print("Row is missing")
    mathmk = [passed, failed]
    return mathmk

# For English
def count_eng_result(header, lines):
    if 'EnglishMarks' not in header:
        print('EnglishMarks column is missing')
    else:
        data = [line.strip().split(',') for line in lines[1:]]

    engmark = header.index('EnglishMarks')
    passed = 0
    failed = 0
    for row in data:
        if len(row) > engmark:
            mk = int(row[engmark])
            if mk < 40:
                failed = failed + 1
            else:
                passed = passed + 1
        else:
            print("Row is missing")
    engmk = [passed, failed]
    return engmk

def plot_all_piecharts(gen, mathmk, engmk):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # Gender Pie Chart
    axs[0].pie(gen, labels=["Male", "Female"], autopct='%1.1f%%')
    axs[0].set_title("Gender")

    # Math Result Pie Chart
    axs[1].pie(mathmk, labels=["Passed", "Failed"], autopct='%1.1f%%')
    axs[1].set_title("Maths Result")

    # English Result Pie Chart
    axs[2].pie(engmk, labels=["Passed", "Failed"], autopct='%1.1f%%')
    axs[2].set_title("English Result")

    plt.show()

def main():
    filepath = "marks.csv"
    lines = read_file(filepath)
    header = read_header(lines)

    gen = count_gender(header, lines)
    math = count_math_result(header, lines)
    eng = count_eng_result(header, lines)

    plot_all_piecharts(gen, math, eng)

main()