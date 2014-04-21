"""
Parse csv file into dictionary
http://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
"""
import csv

def pF(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',', quotechar="'")
        data = dict((rows[0],rows[1]) for rows in reader)
        return data