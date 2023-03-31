from sqlalchemy import ForeignKey,Column, Integer, String, create_engine, func, MetaData
from sqlalchemy.orm import Session, validates, backref, relationship
from .base import Base
from .table_user import User
import sys
import random


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer(), primary_key=True)
    word = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))

    scoring = relationship('Scoring', backref=backref('word'))

    # engine = create_engine('sqlite:///wordle.db', echo=True)
    # Base.metadata.create_all(bind=engine)
    # ession = sessionmaker(bind=engine)
    # session = Session()

    def __repr__(self):
        return f'word(id={self.word},)'
    


# if __name__ == '__main__':
#     engine = create_engine('sqlite:///worlde.db')

    def word_guess(current_user):

        random_list = [ "hench", "pearl", "bench", "hunts", "lunch" ]

        word = random.choice(random_list) 
        random_list = [*word]
        correctword = ["","","","",""]
        print(correctword)
        guesses_left = 5


        while guesses_left > 0:
            guess = input("Guess a word: ").lower()
            guess_list = [*guess]
            if len(guess) == 5:
           
                if guess == word:
                    current_user.update_score()
                    guesses_left = 0
                    print(f"Way to go your score is {current_user.score}!")
                for i in range(5):
                    if guess_list[i] == random_list[i]:
                        correctword[i] = guess_list[i]
                print(correctword)
                guesses_left -= 1
            else:
                print("not valid word. 5 letters please.")

            if guesses_left == 0:
                print(f"You have failed. Sucks to suck. The word was {word}")

    
    
    
    
    
    
    def insert_words(self):
        engine = create_engine('sqlite:///wordle.db')
        with Session(engine) as session:
            session.add(self)
            session.commit()
        