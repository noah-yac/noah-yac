"""
Noah Yacoub

Roulette Number Guessing Function

This is a basic model game of the casino game wheel with red, black and two green tile.

There are 38 tiles in this roulete wheel. 18 red, 18 black, 2 green.

The user will bet money (starting off with $100) each time.
If they win they get 2x what they bet (10x if green) , if they lose they lose what they bet.

In this version of the game the user will guess
'odd' (representive of any black numbers) or
'even' (representive of any red numbers) or
'zero' (representive of any two green tile)

The function generates 2 numbers examples: 25, 02, 36, 17, 00
00 = zero
01,03,05,07,09,11,13,15,17,19,21,23,25,27,29,31,33,35 = odd
02,04,06,08,10,12,14,16,18,20,22,24,26,28,30,32,34,36 = even

"""

def rouletteSpin(money):
    #imports random & sleep module
    import random
    import time

    #define variables
    #money = 100
    IsBetting = True

    print("Roulette Number Guesser")
    print("You have : $", money)
    bet = int(input("\nHow much would you like to bet? (No change/floats accepted please) :"))
    money = money - bet
    guess = input("What would you like to bet on? (odd, even, zero) :")
        
    #while loops keeps betting til out of money
    while IsBetting:
        
        #random number generator
        numb1 = str(random.randint(0,3))
        numb2 = str(random.randint(0,6))
        randomnumber = numb1+numb2
        
        print("\nThe roulete spun and landed on...")
        time.sleep(1)
        
        #converts to int
        randomnumber = int(randomnumber)

        
        #determines generators color
        if randomnumber == 0:
            print(randomnumber, "!! GREEN")
            output = 'g'
        elif randomnumber % 2 == 0:
            print(randomnumber, "!! RED (even)")
            output = 'r'
        elif randomnumber % 2 == 1:
            print(randomnumber, "!! BLACK (odd)")
            output = 'b'
        else:
            print("Invalid input, restart program.")
        
        time.sleep(1)

        #determines if user won or not then calculates winnings/losings
        if output == 'r' and guess == 'even':
            newmoney = money+(bet*2) 
            print("\nWINNER! \nYour $", bet, " bet has been doubled to $", bet*2, "! \nYou now have : $", newmoney)
        elif output == 'b' and guess == 'odd':
            newmoney = money+(bet*2)
            print("\nWINNER! \nYour $", bet, " bet has been doubled to $", bet*2, "! \nYou now have : $", newmoney)
        elif output == 'g' and guess == 'zero':
            newmoney = money+(bet*2)
            print("\nWINNER! \nYour $", bet, " bet has been multiplied by 10 to $", bet*10, "! \nYou now have : $", newmoney)
        else:
            newmoney = money
            print("\nYOU LOSE! \nYour $", bet, " bet has been lost!\nYou now have : $", newmoney)

        #fixes
        money = newmoney

        #checks if balance above $0
        if money < 1:
            IsBetting = False
            print("You've gone broke!")
            break
        
        print("===============================================================================")
        print("Try again!")
        bet = int(input("\nBet: $"))
        money = money - bet
        guess = input("On? (odd, even, zero):")


rouletteSpin(#integer here)
