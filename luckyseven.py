"""
Program: luckyseven.py
Author: Pierre
Date: 09/13/2019

Player will roll a pair of dice, if the dots add up to 7 the player will win 4 dallors otherewise player 
loses 1 dallor.
"""

import random # to generate random number

# function for input validation
def input_validation(money):
    if money < 1:
        return 0

# function to calculate sum of dots on two dice
def Sum(a,b):
    return a+b

# main function
def main():
  
    # true while user wants to play the game
    while True:
        # taking total money from user he/she wants to put in the pot
        total_money = int(input("Enter the amount of money you want to put in pot: "))
      
        # validating the user input
        check = input_validation(total_money)
        if check == 0:
            print("Not enough money to play the game.")
            break
          
        max = 0 # variable to store max amount during game
        i=1 # iteration index
      
        iteration = str(i)
        total = str("${}".format(total_money))
      
        print("Number of rolls"+"          "+"Win or loss"+"          "+"Current value of pot")
        print(iteration.center(15," ")+"Put".center(31," ")+total.center(20,' '))
      
        # paying game till total money is not 0
        while total_money > 0:
            i += 1
            iteration = str(i)
            a = random.randint(1,6) # throwing first die
            b = random.randint(1,6) # throwing second die
            c = Sum(a,b) # caluculating the sum of both die
            # if the sum is 7 (win)
            if c == 7:
                total_money += 4
                total = str("${}".format(total_money))
                print(iteration.center(15," ")+"Win".center(31," ")+total.center(20,' '))
            else:# if player looses
                total_money -= 1
                total = str("${}".format(total_money))
                print(iteration.center(15," ")+"Loss".center(31," ")+total.center(20,' '))
          
            if max < total_money:
                max = total_money

        print("You lost your money after {} rolls of play".format(i))
        print("maximum amount of money in the pot during the playing is ${}".format(max))

        # asking user if he/she want to play again.
        play = (input("Do you want to play again (y/n): "))
        if (play == 'n') or (play == 'N'):
            break;

main()