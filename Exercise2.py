"""
Ayesha Shafquat, Student
Direcotry ID: 113931864
Date: 10-10-2019
Assingment: Midterm Pt 2 Exercise 2

"""

import csv
import os 

#view current directory
os.getcwd()

#change directory 
os.chdir('/Users/Ayesha/Desktop')

# open parks2016.csv by using package csv
parks = csv.reader(open('parks2016.csv'))
# skip the 1st line (header)
next(parks)
# read the rest
for row in parks:
    # convert attendance from string to int
    attendance = int(''.join(row[2].split(',')))
    # calculate adj_attendance
    adj_attendance = attendance-(attendance*0.05)
    # print output
    print("The correct attendance for", row[1], "is", adj_attendance, "not", attendance)


