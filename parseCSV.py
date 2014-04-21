"""
Parse csv file
"""
import csv

def pF(filename):
    with open(filename) as f:
        data = list(tuple(rec) for rec in csv.reader(f, delimiter=','))
        return data