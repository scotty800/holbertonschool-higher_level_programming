#!/usr/bin/python3

""" lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    """Connect to the database and get the states"""

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (mysql_username,  mysql_password, database_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == state_name_to_search).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
