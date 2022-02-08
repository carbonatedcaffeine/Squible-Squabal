# Camden Bruce

#Import the time library and define the costs of the computers
homenum = 900
officenum = 1200
gamernum = 1500
studionum = 2200

# Define the program
print("""
   __  __  __  __  ___     __  __  __  __  ___  _  _  ____  ___  ___     ___  ____  __  ___   ___ 
  (  )(  )(  \/  )/ __)   / _)/  \(  \/  )(  ,\( )( )(_  _)(  _)(  ,)   / __)(_  _)/  \(  ,) (  _)
 __)(  )(  )    ( \__ \  ( (_( () ))    (  ) _/ )()(   )(   ) _) )  \   \__ \  )( ( () ))  \  ) _)
(___/ (__)(_/\/\_)(___/   \__)\__/(_/\/\_)(_)   \__/  (__) (___)(_)\_)  (___/ (__) \__/(_)\_)(___)
 """)
#   Print the details for the computers to the user wanting to buy the computer
print("A home-basic computer is", "$", homenum,"(code - homebasic)")
print("""Specifications:
* 4GB of ram
* Built in Graphics
* 20" Monitor """)
print("\nAn office computer is", "$", officenum,"(code - office)")
print("""Specifications:
* 8GB of ram
* Built in Graphics
* 23" Monitor""")
print("\nA gaming computer is", "$", gamernum,"(code - gamer)")
print("""Specifications:
* 16GB of ram
* 4GB Nvidia graphics card
* 27" Monitor""")
print("\nA studio computer is", "$", studionum,"(code - studio)")
print("""Specifications:
* 16GB of ram
* 4GB Nvidia Quadro graphics card
* Duel 23" Monitors""")

#   Ask for name, age, money and desired computer and set answers as variables. 
name = input("\nWhat is your name? >> ")
age = int(input("\nWhat is your age? >> "))
money = int(input("\nHow much money do you have? >> "))
computer = input("\nWhich computer do you want to buy? >> ")

if computer == 'homebasic':
    if money >= 900:
        print("Come in store to purchase the computer")
    else:
        if money < 900 and age >= 18:
            print("We can give you finance, so if that suits you please come in store, otherwise keep saving")
        else:
            print("Please keep saving then come in store")
                    
if computer == 'office':
    if money >= 1200:
        print("Come in store to purchase the computer")
    else:
        if money < 1200 and age >= 18:
            print("We can give you finance, so if that suits you please come in store, otherwise keep saving")
        else:
            print("Please keep saving then come in store")
                    
if computer == 'gamer':
    if money >= 1500:
        print("Come in store to purchase the computer")
    else:
        if money < 1500 and age >= 18:
            print("We can give you finance, so if that suits you please come in store, otherwise keep saving")
        else:
            print("Please keep saving then come in store")
                
if computer == 'studio':
    if money >= 2200:
        print("Come in store to purchase the computer")
    else:
        if money < 2200 and age >= 18:
            print("We can give you finance, so if that suits you please come in store, otherwise keep saving")
        else:
            print("Please keep saving then come in store")
