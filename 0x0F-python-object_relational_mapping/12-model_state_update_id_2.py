#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    row = session.query(State).filter_by(id='2').first()
    row.name = "New Mexico"
    session.commit()
    session.close()
