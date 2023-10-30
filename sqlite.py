import sqlite3 as s
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import style
# import csv
import pandas as pd
c = s.connect('flash.db')
cur = c.cursor()
cur.execute("Select * from student;")


f = pd.read_csv('flash.csv')
df = pd.DataFrame(f)


def getdata(min1, max1, std):
    for row in std:
        print(row)


mark1 = df.mark1
print(df)
getdata(1,100,cur)