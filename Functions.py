import csv

# This is a simple read csv method, each of the csv files will be read with the same method.

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        return list(reader)


# In order to make the main.py file more readable, separate method aliases will be used for each csv file

# Reads package information from package.csv file
read_package_csv = read_csv

# Reads address information from address.csv file
read_address_csv = read_csv

# Reads the distance information from distance.csv file into a 2d array to hold the distances between each address
read_distance_csv = read_csv
