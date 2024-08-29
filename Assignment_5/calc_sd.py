import math
def calc_standard_deviation(data, avg_cal):
    if not data:
        return 0
    variance = sum((int(row[1])-avg_cal)**2 for row in data)/len(data)
    sd = math.sqrt(variance)
    return sd