#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:55:29 2019

@author: ayesha
"""

# import module for finding working directory (where your files live)
import os

# view current directory
os.getcwd()

# change directory
os.chdir('/Users/Ayesha/Desktop')


# create output file 
urls = open("URL.txt", "w")

#open the file that it will be reading 
with open('aoc2.txt','r') as f:
    #for loop, loops through each line in file to select string that begans with
    #http
    for line in f:
        for word in line.split():
            if "http" in word:
                urls.write('This line contains the following URL: ' + word + "\n")
urls.close()

