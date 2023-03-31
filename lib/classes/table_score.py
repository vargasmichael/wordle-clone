from sqlalchemy import ForeignKey,Column, Integer, String, create_engine, func, MetaData
from sqlalchemy.orm import Session, validates
from .base import Base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)


class Scoring(Base):
    __tablename__ = 'scoring'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    word_id = Column(Integer(), ForeignKey('words.id'))
    win_loss = Column(String())

    def __repr__(self):
        return f'scoring(id={self.id}, ' + \
            f'user_id={self.user_id}, ' + \
            f'word_id={self.word_id}, ' + \
            f'win_loss={self.score})'
    