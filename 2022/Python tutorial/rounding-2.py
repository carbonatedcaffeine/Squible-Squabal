#Camden Bruce
import math # import the math library
distance = int(input("What was the distance: ")) # input the answer as an integer 
time = int(input("What was the time: ")) # input the answer as an integer 
velocity = math.ceil(distance / time) # calculate the velocity and round up to the nearest full number
print("The velocity is",velocity) # print the velocity
