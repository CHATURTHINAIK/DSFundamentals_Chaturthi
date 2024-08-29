def highest_per_day(data):
    if not data:
        return 0
    cal_per_day = {}
    for row in data:
        date = row[0]
        calories = int(row[1])
        if date in cal_per_day:
            cal_per_day[date] += calories
        else:
            cal_per_day[date] = calories
    highest_day = None
    highest_cal = 0
    for date, total_cal in cal_per_day.items():
        if total_cal>highest_cal:
            highest_day = date
            highest_cal = total_cal
    hpd = [highest_day, highest_cal]
    return hpd