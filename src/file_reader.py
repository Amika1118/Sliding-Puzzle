import csv
import os

location_01 = {"x":[], "y":[]}
location_02 = {"x":[], "y":[]}
location_03 = {"x":[], "y":[]}
location_04 = {"x":[], "y":[]}

with open("../data/winning_locations.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    reader.__next__()
    for row in reader:
        if row[0] == "location_01":
            location_01["x"].append(row[2::2])
            location_01["y"].append(row[3::2])

