#!/usr/bin/python3

#!/usr/bin/python3
# Lists all State objects from the database hbtn_0e_6_usa.
# Usage: ./10-model_state_fetch_all.py <mysql username> /
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
    state_name_to_search = argv[4]
    Session = sessionmaker(bind=engine)    
    session = Session()

    state = session.query(State).filter(State.name == state_name_to_search).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
