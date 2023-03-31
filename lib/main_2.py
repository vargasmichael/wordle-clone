from sqlalchemy import create_engine, Column, Integer, String
from classes.table_user import User
from classes.table_score import Scoring
from classes.table_word import Word
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random
from collections import Counter

Base = declarative_base()



engine = create_engine('sqlite:///wordle.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

def register(username, password):
    hashed_password = generate_password_hash(password)
    user = User(username=username, password=hashed_password)
    session.add(user)
    session.commit()
    print(f'User {username} has been registered.')

def login(username, password):
    user = session.query(User).filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return False
    login_user(user)
    print(f'Welcome, {username}!')
    return True

def logout():
    logout_user()

def play():
    print('Welcome to Wordle Clone!')
    word = random.choice(session.query(Word).all()).word
    guesses = []
    while True:
        guess = input('Enter your guess (5 letters): ').lower()
        if guess == 'quit':
            break
        if len(guess) != 5 or not guess.isalpha():
            print('Invalid guess. Please enter a 5-letter word.')
            continue
        if guess in guesses:
            print(f'You already guessed {guess}.')
            continue
        guesses.append(guess)
        if guess == word:
            print('Congratulations, you won!')
            break
        else:
            counts = Counter(word)
            matches = [c for c in guess if c in counts]
            print(f'{len(matches)} letter(s) match.')
    print(f'The word was {word}.')

if __name__ == '__main__':
    with Session(engine) as session:
        print('''

##      ##  #######  ########  ########  ##       ######## 
##  ##  ## ##     ## ##     ## ##     ## ##       ##       
##  ##  ## ##     ## ##     ## ##     ## ##       ##       
##  ##  ## ##     ## ########  ##     ## ##       ######   
##  ##  ## ##     ## ##   ##   ##     ## ##       ##       
##  ##  ## ##     ## ##    ##  ##     ## ##       ##       
 ###  ###   #######  ##     ## ########  ######## ######## 

''')
        while True:
            print('''
            1. Register
            2. Login
            3. Quit
            ''')
            choice = input('Enter your choice: ')
            if choice == '1':
                username = input('Enter a username: ')
                password = input('Enter a password: ')
                register(username, password)
            elif choice == '2':
                username = input('Enter your username: ')
                password = input('Enter your password: ')
                if login(username, password):
                    play()
                    logout()
            elif choice == '3':
                break
            else:
                print('Invalid choice. Please try again.')
