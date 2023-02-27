
import csv

## Opening the file in read-only mode. airtravel.csv is in the same directory with the python script

with open('airtravel.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)     # using a csv.reader object

    next(reader)  # skipping the first line

    for row in reader:
        print(row)












