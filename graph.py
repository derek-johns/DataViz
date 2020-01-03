from collections import Counter
import numpy as np
import geojson
import matplotlib.pyplot as plt
import csv

MY_FILE = "./sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    '''Parses a raw CSV file to a JSON-line object'''

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list
    parsed_data = []

    # Skip over first line of file for headers
    fields = csv_data.next()

    # Iterate over each row of csv file
    # zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV file
    opened_file.close()

    return parsed_data


def visualize_days():
    '''Visualize data by day of week'''

    # grab our parsed data
    data_file = parse(MY_FILE, ",")

    # make new variable "counter" from iterating through each
    # line of data in the parsed data
    # count how many incidents happen on each day of week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # separate the x-axis data from the "counter" variable from
    # the y-axis data
    data_list = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
    ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # with y-axis data, assign it to matplotlib plot instance
    plt.plot(data_list)

    # create the amount of ticks needed for our x-axis and
    # assign labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # save plot
    plt.savefig("Days.png")

    # close plot file
    plt.clf()

def visualize_type():
    '''Visualize data by category in a bar graph'''

    # grab our parsed data
    data_file = parse(MY_FILE, ",")

    # make a new variable, 'counter', from iterating through each line
    # of data in the parsed data, and count how many incidents happen 
    # by category
    counter = Counter(item["Category"] for item in data_file)

    # set the label based on keys of counter
    # order does not matter so we can use counter.keys()
    labels = tuple(counter.keys())

    # set exactly where the labels hit the x-axis
    xlocations = np.array(range(len(labels))) + 0.5

    # width of each bar that will be plotted
    width = 0.5

    # assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # assign labels and tick locatin to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # give some more room so the x-axis labels aren't cut off
    plt.subplots_adjust(bottom=0.45)

    # make overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # save graph
    plt.savefig("Type.png")

    # close plot
    plt.clf()

def main():
    visualize_type()

if __name__ == "__main__":
    main()