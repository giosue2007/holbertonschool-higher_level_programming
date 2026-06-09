#!/usr/bin/python3
"""
This module lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Connexion à la base de données MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Ouverture de la session ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête ORM avec un filtre pour chercher la lettre 'a'
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    # Affichage des résultats
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Fermeture de la session
    session.close()
