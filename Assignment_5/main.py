from read import *
from filterdata import *
from calc_avg import *
from calc_sd import *
from highestperday import *
from highest_day_cal import *
from input import *
from output import *
def main():
    filepath = 'calories_data.csv'
    # reading data from csv file
    data = read_file(filepath)

    from_date, to_date = take_input()

    # filtering data based on from_date and to_date
    filtered_data = filter_data(data, from_date, to_date)

    # operations on filtered data
    avg_cal = calc_avg_cal(filtered_data)
    sd = calc_standard_deviation(filtered_data, avg_cal)
    hc = highest_cal(filtered_data)
    hd = highest_per_day(filtered_data)
    # displaying output
    display_output(from_date, to_date, avg_cal, sd, hd, hc)

main()