import csv as c

with open('../flash.csv') as file:
    reader = c.reader(file)
    for row in reader:
        print(row)
