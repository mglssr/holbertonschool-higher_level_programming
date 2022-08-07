#!/usr/bin/python3
"""Write a script that changes the name of
a State object from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import Session

    user = sys.argv[1]
    passwrd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(user, passwrd, dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    update_obj = session.query(State).get(2)
    update_obj.name = "New Mexico"
    session.commit()
    session.close()
