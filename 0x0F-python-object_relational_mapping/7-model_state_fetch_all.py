#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
	engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}?host=localhost?port=3306".format(argv[1], argv[2], argv[3])
	Base.metadata.create_all(bind=engine)
	Session = sessionmaker()
	Session = sessionmaker(bind=engine)
	for state in Session.query(state).orderby(State.id):
		print("{}: {}".format(state.id, state.name))
	session.close()
