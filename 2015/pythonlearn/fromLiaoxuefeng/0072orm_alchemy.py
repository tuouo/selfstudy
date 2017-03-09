#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# need 'pip install sqlalchemy'
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):				# if more than one table, more class
    __tablename__ = 'user'
	
    id = Column(String(20), primary_key = True)
    name = Column(String(20))
	
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')
					#sql type + sql drive name://username:password@machine IP:port/sql name 
DBSession = sessionmaker(bind = engine)


session = DBSession()
new_user = User(id = '5', name = 'Lily')
session.add(new_user)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id == '5').one()	# all()
print('type:', type(user))
print('name:', user.name)
session.close()

##################################################################
# class User(Base):				
    # __tablename__ = 'user'
	
    # id = Column(String(20), primary_key = True)
    # name = Column(String(20))
    # books = relationship('Book')						# one to many
	
# class Book(Base):
    # __tablename__ = 'book'
	
    # id = Column(String(20), primary_key = True)
    # name = Column(String(20))
    # user_id = Column(String(20), ForeignKey('user.id'))	# many connect to one
	
#	#in this way, when we inquire User, he's books will return in list