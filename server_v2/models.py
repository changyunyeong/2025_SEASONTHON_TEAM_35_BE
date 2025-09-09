from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Question(Base): # database 상속
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True, index=True)
    conent = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref = "answers") # backref: 역참조