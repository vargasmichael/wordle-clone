from sqlalchemy import (create_engine, desc,
    Index, Column, Integer, String)
# from sqlalchemy.ext.declarative import ,declarative_base
from sqlalchemy.orm import Session,declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(), unique=True)
    password = Column(String())
    score = Column(Integer())

    # scoring = relationship('Scoring', backref=backref('user'))

    def __repr__(self):
        return f'username(id={self.username}, ' + \
            f'score={self.score})'
    
    # add a user
    def add_to_user(self):
        engine = create_engine('sqlite:///wordle.db')
        with Session(engine) as session:
            session.add(self)
            session.commit()

    # update an object    
    # def update_score(self):
    #     engine = create_engine('sqlite:///wordle.db')
    #     with Session(engine) as session:
    #         session.query(User).filter(User.id == self.id).update({User.score: User.score + 1})
    #         session.commit()

    def update_score(self):
        engine = create_engine('sqlite:///wordle.db')
        with Session(engine) as session:
            session.query(User).filter(User.id == self.id).update({User.score: User.score + 1})
            session.commit()
            # Fetch the updated User instance from the database
            updated_user = session.query(User).filter(User.id == self.id).one()
            # Update the score attribute of the User instance in memory
            self.score = updated_user.score




    #delete a user   
    def delete_user(self):
        engine = create_engine('sqlite:///wordle.db')
        with Session(engine) as session:
            session.query(User).filter(User.id == self.id).delete()
            session.commit()

    #query login
    @classmethod
    def login(cls, username, password):
        engine = create_engine('sqlite:///wordle.db')
        with Session(engine) as session:
            user = session.query(User).filter(User.username==username, User.password==password).first()
            if user:
                return user
            else:
                return False

    #search for score     
    @classmethod
    def search_score(cls, username, score):
        engine = create_engine('sqlite:///wordle.db')
        with Session(engine) as session:
            user = session.query(User).filter(User.score == score, User.username == username).first()
            if user:
                return user
            

    
    
    
       
       
if __name__ == '__main__':
    engine = create_engine('sqlite:///wordle.db')
    Base.metadata.create_all(engine)


    with Session(engine) as session:
        user = session.query(User).filter(User.id == 2).first()
            
    

    # with Session(engine) as session:
    #     score = 


    michael_vargas = User(
        username="Michael Vargas",
        password="123",
        score="85"
    )

# session.add(michael_vargas)
# session.commit()

# my_user = User()
# print(f"Your score is {michael_vargas.score}.")

