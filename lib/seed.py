
from sqlalchemy import *
from sqlalchemy.orm import *
from classes.table_user import User
from classes.table_score import Scoring
from classes.table_word import Word
from classes.base import Base


engine = create_engine('sqlite:///worlde.db')
User.__table__.drop(engine)
Word.__table__.drop(engine)
Scoring.__table__.drop(engine)
Base.metadata.create_all(engine)
with Session(engine) as session:

    u1 = User(username = "Michael Scott", password="password")
    u1 = User(username = "Creed", password="whatsapassword")
    u1 = User(username = "Dwight", password="th1s1smyp@assw0rd")
    word = Word(word = "")
    

