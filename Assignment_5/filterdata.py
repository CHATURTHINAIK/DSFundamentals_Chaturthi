def filter_data(data, from_date, to_date):
    filtered_data = [row for row in data if from_date<=row[0] <= to_date]
    return filtered_data