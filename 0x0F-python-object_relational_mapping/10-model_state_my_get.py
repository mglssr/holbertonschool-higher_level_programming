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
    dbname = sys.argv[3]
    stname = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(user, passwrd, dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == "{}".format(stname))
    if state:
        for st in state:
            print(st.id)
    else:
        print("Not found")
    session.close()
