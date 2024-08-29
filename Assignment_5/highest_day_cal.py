def highest_cal(data):
    if not data:
        return 0
    highest_cal = int(data[0][1])
    for row in data:
        calories = int(row[1])
        if calories > highest_cal:
            highest_cal = calories
    return highest_cal