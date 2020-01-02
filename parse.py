import numpy
import geojson
import matplotlib
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


def main():
    # Call our parse function and give needed parameters
    new_data = parse(MY_FILE, ",")

    print new_data

if __name__ == "__main__":
    main()