from sqlalchemy import *
from sqlalchemy.orm import *
from classes.table_user import User
from classes.table_score import Scoring
from classes.table_word import Word
from classes.base import Base
import random


if __name__ == '__main__':
    engine = create_engine('sqlite:///worlde.db')
    print(''''

##      ##  #######  ########  ########  ##       ######## 
##  ##  ## ##     ## ##     ## ##     ## ##       ##       
##  ##  ## ##     ## ##     ## ##     ## ##       ##       
##  ##  ## ##     ## ########  ##     ## ##       ######   
##  ##  ## ##     ## ##   ##   ##     ## ##       ##       
##  ##  ## ##     ## ##    ##  ##     ## ##       ##       
 ###  ###   #######  ##     ## ########  ######## ######## 

''')

#Checks for user existence

    inprogram = True
    while inprogram:
        userinput1 = input("Do you have a username. yes/no: ")
        #user inputer
        if userinput1 == "no":
            i1= input("Pick a username: ")
            i2= input("Pick a password: ")
            User(username=i1, password=i2, score= 0).add_to_user()
            
        elif userinput1 == "yes":
           username = input("Enter your username: ")
           password = input("Enter your password: ")
           User.login(username, password)
           current_user = User.login(username, password) 
           print(current_user)
        else:
            print('Login failed')
        inprogram = False

    # while inprogram:
        userinput2 = input(
            '\n Select a number \n 1) New Game:  \n 2) Check Score: \n 3) Delete User: \n')
        if userinput2 == "1":
            print("Lets do this!")
            Word.word_guess(current_user)
        elif userinput2 == "2":
            score = current_user.score
            User.search_score(username, score)
            print(f"Your score is {current_user.score}.")
        elif userinput2 == "3":
            self = current_user
            User.delete_user(self)
            print(f"Bye {current_user.username}")
        inprogram = False

        
#bugs- if username or password isn't correct send it back to the main prompt
# show letters that are correct but no in the right spot
# show incorrect letters that have been guessed 
       
                    

                