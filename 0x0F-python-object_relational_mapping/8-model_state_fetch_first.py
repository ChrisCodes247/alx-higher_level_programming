#!/usr/bin/python3

#!/usr/bin/python3
# Lists the first State object from the database hbtn_0e_6_usa.
# Usage: ./8-model_state_fetch_all.py <mysql username> /
#                                     <mysql password> /
#                                     <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).first():
        print("{}: {}".format(state.id, state.name))

    session.close()
