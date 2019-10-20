##################################
# Name: Ayesha Shafquat, Student # 
# Direcotry ID: 113931864        #
# Date: 10-14-2019               #
# Assingment: Module 6 Exercise  # 
##################################


#header of the class  
class Car():
    #class docstring
    '''
    Attributes:
        x(float): 0
        y(float): 0
        gasoline(float): 10.0
    '''
    def __init__(self, x, y, gasoline): #definition function that sets the attributes for the class 
        self.x = x
        self.y = y
        self.gasoline = gasoline
        
    # creating the mdrive() method 
    def drive(self, direction):
        if self.gasoline == 0:
            print("You are out of gas") #if gas is 0 it will say you are out of gas 
            return
        else:
            # fixes the case sensitvity 
            direction = direction.lower()
            # else it changes the x or y attribute accoridng to the specified direction
            if direction == 'n':
                self.y += 1       
            elif direction == 's':
                self.y -= 1
                print('s')
            elif direction == 'e':
                self.x += 1
                print('e')
            elif direction == 'w':
                self.x -= 1
                print('w')
            self.gasoline -= 0.1
            print(f'Attributes: y={self.y}, x={self.x}\n direction:{direction}\n gasoline={self.gasoline}')

# testing the objects
mycar = Car(0,0,19)
mycar.drive(direction='n')