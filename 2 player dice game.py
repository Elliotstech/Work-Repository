#Lists
users =["Elliot", "Obama"]  #---Username list
passwords =["KiTty", "Gone"] #---Password list

#Imported Modules
import time
import random

#Define
Activated = False
counter = 0
warning = 0
score = 0
score2 = 0

#assignment
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total = 0
total2 = 0
roundtotal = dice1 + dice2
playerround = 0

print("Please log into your account.")  
existinguser = input("Do you have an account?: ") #---Asking if existing user
if existinguser == "yes" or existinguser == "Yes": #---if answer is yes
    while not Activated: 
        counter = counter + 1
        if counter < 4:
            try:
                user = input("Username 1: ") #---ask for username 1
                Pass = input("Password 1: ") #---ask for password 1
                if user in users: #---If username in users
                    if users.index(user) == passwords.index(Pass): #---Make them corrisponding
                        print("Login in suceeded welcome", user)
                        user2 = input("Username 2: ") #---ask for username 2
                        pass2 = input("Password 2: ") #--- ask for password 2
                        if user in users: #---If username in users
                            if users.index(user) == passwords.index(Pass): #---Make them corrisponding
                                print("Login in suceeded welcome", user, user2)
                                print("Have fun with the game!")
                        Activated = True
                    else:
                        print("Invalid password. You have had tries:" , counter) #---Error message for invalid password
                else:
                    print("Invalid username. You have had tries:" , counter) #---Error message for invalid username
            except ValueError:
                print("Value Error. You have had tries:" , counter) #---Error message for value error
        else:
            print("Kicked") 
            time.sleep(10)
            counter = 0
            warning = warning + 1
            print("warning number:" , warning)
            if warning > 3:
                time.sleep(1)
                print("You have been locked out.")
                warning = 0
                
else:
    while Activated == False:
        newuser = input("Enter a username: ")
        if newuser in users:
            print("This username has already been taken")
        else:
            users.append(newuser)
            newpass = input("Enter a password: ")
            passwords.append(newpass)
            print(users)
            print(passwords)
            Activated = True


logindice = input("Do you want to play the dice game?: ") #---Start of round loop for dice game
if logindice == "Yes" or logindice == "yes": 
    while playerround < 5:
        playerround = playerround + 1
        startround = input("Would you like the start the next round?: ")
        if startround == "Yes" or "yes":
            print(user, "rolled the first dice: " , dice1)
            print(user, "rolled the second dice: " , dice2)
            if roundtotal % 2 == 0: #---If an even number is rolled
                roundtotal = roundtotal + 10 #---Add 10 points to the round total
                print("You have been rewarded 10 points for roling an even number.")
                print("Your total points: " , total)
                dice1 = random.randint(1,6) #---Dice are random numbers from 1-6
                dice2 = random.randint(1,6)
                if roundtotal < 0:
                    roundtotal = 0
            elif roundtotal % 2 > 0: #---If a odd number is rolled
                roundtotal = roundtotal - 5
                print ("you have been reducing 5 points for rolling an odd number.")
                print("Your total points: " , total)
                dice1 = random.randint(1,6)
                dice2 = random.randint(1,6)
                if roundtotal < 0:
                    roundtotal = 0
        total = roundtotal + total
        if roundtotal % 2 == 0: #---If an even number is rolled
            roundtotal = roundtotal + 10
            print("You have been rewarded 10 points for roling an even number.")
            print("Your total points: " , total)
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            if roundtotal < 0:
                roundtotal = 0
        elif roundtotal % 2 > 0: #---If a odd number is rolled
            roundtotal = roundtotal - 5
            print ("you have been reduced by 5 points for rolling an odd number.")
            print("Your total points: " , total)
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            if roundtotal < 0:
                roundtotal = 0
    total2 = roundtotal + total2

#This is my latest project and is still in progress
