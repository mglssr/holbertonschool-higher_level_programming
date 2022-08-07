#!/usr/bin/python3
"""Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""


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
    s1 = State(name="Louisiana")
    session.add(s1)
    session.commit()
    print(s1.id)
    session.close()
