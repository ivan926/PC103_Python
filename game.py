import random


print("Welcome to the game of life")

print("You will be given a series of scenerios to choose from")

print("Your choices will have consequences")

print("Choice options will range from letters A to C")

print()

print("You are home and you should be doing your computer science lab")

user_choice = input("Will you \n (A) PLAY VIDEO GAMES INSTEAD  \n (B) DO YOUR CS LAB HOMEWORK ")

# main if else

if user_choice == 'A' or user_choice == 'a':
    print()
    print("You have chosen the easy path, the dark side has overcome you \nYou have turned to the dark side")

    user_choice = input("Will you further go down the path of least resistence?\n \n Will you \n (A) CONTINUE DOWN THE PATH OF DARKNESS \n (B) CHOOSE TO RESIST TEMPATION AND RETURN TO THE LIGHT SIDE ")
    
    #branched if else
    if user_choice == 'A' or user_choice == 'a':
        print()
        print("You have been give the title of darth twinkle toes")
        print("You now only perpetually feel pain and suffering in your life")

        #OPTION THAT HAS THREE CHOICES
        print()
        user_choice = input("You are feeling cynical \nYou have just invaded a planet full of ewoks on Endor, will you \n (A) SLAUGHTER ALL THE POOR INHABITANTS \n (B) BE MERCIFUL \n (C) LEAVE IT TO CHANCE AND ROLE THE DICE")
        if user_choice == 'A' or user_choice == 'a':
            print()
            print("You grow in anger and hatred and sadness, this fuels you towards UNLIMITED POWER!")
            
        elif user_choice == 'B' or user_choice == 'b':
            print()
            print("For some strange reason you forgot about slaughtering the ewoks")
        #THIRD CHOICE BELOW
        elif user_choice == 'C' or user_choice == 'c':
            print()
            print("You begin to role the dice")
            print()
            print("It is a 4 sided die, if it rolls greater than 2 the planet will be destroyed by the deathstar \n\nTis below a three, we wipe half the population")
            print()
            print("The result.....")
            dice_number = random.randint(1,4)
        

            if dice_number > 2:
                print()
                print("You fire the deathstar and the planet is olbiterated into tiny pieces")
            elif dice_number < 3:
                print()
                print("In typical Thanos fashion, you wipe half the population, congratulations lord twinkle toes, you have added balance to this part of the galaxy")
            else: 
                print("Wrong option")

        else: 
            print("Wrong option")


    #branched if else
    elif user_choice == 'B' or user_choice == 'b':
        print()
        print("You have chosen happiness \nYou feel never ending bliss corsing through your veins")
    else: 
        print("Wrong option")


# main if else  
elif user_choice == 'B' or user_choice == 'b':

    print()
    print("You have chosen the right path\n \nThrough that small act, you have gained the momentum and confidence to take up other projects")
    print("Because of your efforts, you have been given an opportunity to join an internship\n")

    user_choice = input("You have been given the option to choose \n (A) JOIN MICROSOFT\n (B) JOIN ROBINHOOD")

    #branched if else
    if user_choice == 'A' or user_choice == 'a':
        print()
        print("CONGRATULATIONS, you have joined a FANG company, you are making over 100K a year and get free lunh")
        print("You are now however stuck in golden hand cuffs that you never want to leave, and find yourself spending less time with your family\n")
        
        user_choice = input ("Will you \n (A) LEAVE YOUR JOB \n (B) WILL YOU CONTINUE ONWARD")

        if user_choice == 'A' or user_choice == 'a':
            print()
            print("You have saved your marriage, you live your life in happiness for the next 40 years until you die")
            print("You have also sold some stock in microsoft which gives you enough to take your family on a nice trick to Europe")
        elif user_choice == 'B' or user_choice == 'b':
            print()
            print("Sadly your wife divorces you \nYou are very rich by the time you die thanks to some exceptional investments \nbut you die sad and alone")
        else: 
            print("Wrong option")



    #branched if else

    #BELOW I ALSO PRESENT THREE POSSIBLE OPTIONS
    elif user_choice == 'B' or user_choice == 'b':
        print()
        print("CONGRATULATIONS, you are making a hefty amount of money, and after a couple of months your company has an IPO, \nyou make an extra million dollars in a matter of minutes\n")

        user_choice = input("Will you \n (A) USE YOUR MONEY TO INVEST IN REAL ESTATE AND THE STOCK MARKET \n (B) HIDE YOUR EARNINGS UNDER YOUR BED \n (C) GIVE 70 PERCENT OF YOUR INCOME TO CHARITY ")

        if user_choice == 'A' or user_choice == 'a':
            print()
            print("You have struck gold, you are able to retire before the age of 40")
            
        elif user_choice == 'B' or user_choice == 'b':
            print()
            print("Your house burns down and you lose everything, your retirement is not possible and you work until you die")
        #THIRD CHOICE BELOW
        elif user_choice == 'C' or user_choice == 'c':
            print()
            print("You die poor, but are given the keys to the celestial kingdom and recieve exaltation")
        else: 
                print("Wrong option")
    else: 
        print("Wrong option")
else: 
        print()
        print("Wrong option")
#end of program
print()
print("Game has ended")







    


    
