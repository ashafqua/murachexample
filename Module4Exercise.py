#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Ayesha Shafquat, Student 
Directory ID: 113931864
Date: 09-23-2019 
Assingment: Module 4 Exercise 

"""

#find the path of your file, and change it if needed 
import os
os.getcwd()
os.chdir('/Users/ayesha/desktop/INST326')

def text(infile, outfile):
    #create input file that will open the input file for reading, using the file objects
    infile=open('mod4.txt')
    #create a output file that will open the output file for writing, using the file objects
    outfile=open('2mod4.txt','w')
    #the for loop will loop through each line in the file 
    for line in infile:
        #the if statement selects the first letter of the line 
        if line[0].isupper():
            print(line,file=outfile)˜
    #the 2 lines below will close the file
    infile.close()
    outfile.close()
    
#call the function
text(infile, outfile)