#!/usr/bin/python3
"""Write a script that lists all State objects
from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import Session

    user = sys.argv[1]
    passwrd = sys.argv[2]
    dbname = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
                '.format(user, passwrd, dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
