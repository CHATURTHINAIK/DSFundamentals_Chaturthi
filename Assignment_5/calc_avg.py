def calc_avg_cal(data):
    if not data:
        return 0
    total_cal = 0
    for row in data:
        total_cal = total_cal + int(row[1])

    avg_cal = total_cal/len(data)
    return avg_cal