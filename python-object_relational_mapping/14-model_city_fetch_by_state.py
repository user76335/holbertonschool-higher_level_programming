#!/usr/bin/python3
"""
Lists all State objects from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    username, password, db_name = (sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True,
    )

    session = Session(engine)
    cities = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
