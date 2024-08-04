#Camden Bruce
import math # import math and time libraries
import time

def main(): # lists the selection menu, takes answer, and prompts an error if there is an incorrect input.
    ans = input("""
Calculate derived units
[##############################################]
Enter the code in the brackets for the unit you want to calculate.

* speed / velocity (v)

* acceleration (a)

* force (N)

* pressure (Pa)

> """)
    if ans == 'v':
        velocity()
    if ans == 'a':
        acceleration()
    if ans == 'N':
        force()
    if ans == 'Pa':
        pressure()
    else:
        print("\nErr: Not a correct input")
        time.sleep(1)
        main()

#input the answer as an integer, calculate and round up to the nearest full number
def velocity():
    distance = int(input("What was the distance: "))
    time = int(input("What was the time: "))
    velocity = math.ceil(distance / time)
    print("velocity =",velocity,"ms^-1")

def acceleration():
    velocity = int(input("What was the velocity: "))
    time = int(input("What was the time: "))
    acceleration = math.ceil(velocity / time)
    print("acceleration =",acceleration,"ms^-2")

def force():
    mass = int(input("What was the mass: "))
    acceleration = int(input("What was the acceleration: "))
    force = math.ceil(mass * acceleration)
    print("force =",force,"N")

def pressure():
    force = int(input("What was the mass: "))
    area = int(input("What was the acceleration: "))
    pressure = math.ceil(force / area)
    print("pressure =",pressure,"Pa")

main()