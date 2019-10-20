"""
Ayesha Shafquat, Student
Direcotry ID: 113931864
Date: 10-10-2019
Assingment: Midterm Pt 2 Exercise 2

"""

#Function air_bnb calculates cost of room, takes the argument days 
def air_bnb(days):
    cost=(days*110)+50 #formula for cost, 110 per day + $50 cleaning fee 
    return cost


#Function soutwest_ticket calculates cost of ticket, takes city as argument 
def southwest_ticket(city):
    if city == 'Atlanta': #if city= Atlanta, price is $222 
        return 222
    elif city == 'Miami': #if city = Miami, price is 300 
        return 300
    elif city == 'New York': #if city = New York, price is 150 
        return 150
    else:                     #else, the price of Houston is returned 
        return 475


#Function car_rental, calculates cost of car, takes days as argument 
def car_rental(days):
    if days >= 7:
        return (44 * days)-55
    if days >=3:
        return (44 * days)- 25
    else:
        return (44 * days) 
    
#Function total_vacation created to tell you the cost of room, ticket, and car
def total_vacation(city, days):
    return air_bnb(days) + southwest_ticket(city) + car_rental(days)


# Test vacation to Atlanta for 10 days 
print("Total for vacation to Atlanta: ", total_vacation('Atlanta', 10))

