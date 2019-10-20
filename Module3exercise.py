##################################
# Name: Ayesha Shafquat, Student # 
# Direcotry ID: 113931864        #
# Date: 09-16-2019               #
# Assingment: Module 3 Exercise  # 
##################################

#Part Two:
def UpLo():    # create function 
    word = input("Enter a word: ") # ask user for input 
    first_letter = str(word[0]).upper() 
    after = first_letter + word[1:]   
    print("Before: {0} After: {1}".format(word, after)) # use format method to make first letter uppercase
UpLo()


#Part Three: 
sentence = input("Enter a sentence: ") #ask user to input a sentence 
split_sentence = sentence.split() #splits the sentence 
for i in split_sentence:
 print(str(i[0]).upper() + str(i[1:])) #prints word by word


#Part Four:
# Initiating count and variables
maxsolar = 0
maxwind = 0
solar_state = ""
wind_state = ""
for key1,value1 in energy_2009.items(): # loop to iterate through the dictionary
    for key2,value2 in value1.items(): # loop to loop through the nested dictionary
        if key2 == "solar":
            if value2 > maxsolar: #Keeps track of the largest number for solar and it's associated state
                maxsolar = value2
                solar_state = key1
                
     
        if key2 == "wind":
            if value2 > maxwind:  #Keeps track of the largest number for wind and it's associated state
                maxwind = value2
                wind_state = key1
 
print(solar_state, "is the state with the highest solar generation in 2009 with", maxsolar, "megawatts")               
print(wind_state, "is the state with the highest wind generation in 2009 with", maxwind, "megawatts")

