#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Name: Ayesha Shafquat
Directory ID: 113931864
Date: 2019-11-09
Assignment: Homework 1
'''

QUESTIONS = ["2 + 2", "10 // 5", "8 == 2 ** 3", "5 % 2 == 0"]
ANSWERS = ["4", "2", "True", "False"]

def main():
    count = 0 #Starting index for ANSWERS list
    correct_counter = 0
    incorrect_counter = 0

    for i in QUESTIONS:
        print([i])
        user_answer = input("Enter the answer: ")

       
        if user_answer == ANSWERS[count]:
            print("That is the correct answer")
            correct_counter = correct_counter + 1
        else:
            print("Incorrect answer!")
            incorrect_counter = incorrect_counter + 1

        count = count + 1 #counts the number of questions

    print("You got " + str(correct_counter) + " question(s) correct! \n")
    count = correct_counter + incorrect_counter
    print("You answered " + str(count) + " questions total.")
    percentage = (correct_counter / count)
    print("Percentage: " + str(percentage))

main()
