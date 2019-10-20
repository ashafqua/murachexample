'''
Name: Ayesha Shafquat
Directory ID: 113931864
Date: 09-25-2019
Assignment: Homework 2
'''

#import csv module 
import csv

#open and read the file, put content into dictionary 
f=open('energy.csv', 'r')
sheet=csv.DictReader(f)

#initiate count and variables 
maxSolar=0
maxWind=0
S_state=''
W_state=''

#create for loop to iterate through the dictionary
for row in sheet:
    #created loop to loop through nested dictionary
    for key, value in row.items():
        #created conditionals to keep track of the largest number for solar and wind and it's associated state
        if key=="Solar":
            if float(value) > float(maxSolar):
                maxSolar=value
                S_state=row['State']
            
        if key=="Wind":
            if float(value) > float(maxWind):
                maxWind=value
                W_state=row['State']

print('The largest producer of wind power was', W_state, 'at', maxWind, 'Megawatthours.')
print('The largest producer of solar power was', S_state, 'at', maxSolar, 'Megawatthours.')

f.close()